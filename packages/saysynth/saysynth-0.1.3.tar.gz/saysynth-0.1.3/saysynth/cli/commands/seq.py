"""
Play a sequence of `chord`, `midi`, `note`, and/or `arp` tracks via yaml configuration.
"""

import copy
import os
from argparse import ArgumentError
from multiprocessing.pool import ThreadPool as Pool

import click
import yaml

from saysynth.cli.colors import blue, green, red, yellow
from saysynth.cli.commands import arp, chord, midi, note
from saysynth.cli.options import seq_command_arg, seq_opts
from saysynth.lib import controller


def run(**kwargs):
    controller.ensure_pid_log()
    config_path = kwargs.pop("base_config")
    command = kwargs.pop("command")
    output_dir = kwargs.pop("output_dir", "./")
    if config_path:
        # print config
        if command == "echo":
            click.echo(str(config_path.read()))
            return
        base_config = yaml.safe_load(config_path)
    else:
        base_config = {"name": "*"}
    config_overrides = kwargs.get("config_overrides", {})
    globals = base_config.pop("globals", {})
    seq = base_config.pop("name", None)
    if seq is None:
        raise ArgumentError("You must set a `name` in your sequence config")

    tracks = kwargs.get("tracks") or []
    audio_devices = kwargs.get("audio_devices") or []

    # play/start sequences/tracks
    if command in ["play", "start", "render"]:
        track_configs = []
        for track, base_track_config in base_config.get("tracks", {}).items():

            # optionally skip tracks
            if len(tracks) and track not in tracks:
                continue

            # allow for track-specific overrides
            track_overrides = config_overrides.pop(track, {})
            config_overrides.update(track_overrides)

            # create track config
            track_options = copy.copy(globals)  # start with globals
            track_options.update(
                base_track_config.get("options", {})
            )  # override with base track configs
            track_options.update(config_overrides)

            # optionally start tracks immediately
            if command == "start":
                track_options["start_count"] = 0

            # optionally render tracks
            if command == "render":
                os.makedirs(output_dir)
                track_options["audio_output_file"] = os.path.join(
                    output_dir, f"{seq}-{track}-{base_track_config['type']}.aiff"
                )

            base_track_config["options"] = track_options
            ad = track_options.get("audio_device", None)
            if not len(audio_devices) or ad in audio_devices:
                track_configs.append((seq, track, ad, base_track_config))

        # run everything
        for _ in Pool(len(track_configs)).imap(run_track_func, track_configs):
            continue

    if command == "stop":

        if len(audio_devices):
            for ad in audio_devices:
                click.echo(f"🛑 {red('stopping')} all tracks on  {yellow('audio_device')}: {blue(ad)} in {yellow('sequence')}: {blue(seq)}", err=True)
                controller.stop_child_pids(seq, track=None, ad=ad)

        else:
            if not len(tracks):
                tracks = ["*"]
            for track in tracks:
                click.echo(f"🛑 {red('stopping')} {yellow('track')}: { blue(track)} in {yellow('sequence')}: { blue(seq) }", err=True)
                controller.stop_child_pids(seq, track)


def run_track_func(item):
    seq_name, track, ad, kwargs = item
    pid = os.getpid()
    parent_pid_file = controller.add_parent_pid(seq_name, track, ad, pid)
    type = kwargs.get("type", None)
    options = kwargs.get("options", {})
    options["parent_pid"] = pid  # pass parent id to child process.
    options["parent_pid_file"] = parent_pid_file

    TRACK_FUNCS = {
        "chord": chord.run,
        "midi": midi.run,
        "note": note.run,
        "arp": arp.run,
    }

    if type not in TRACK_FUNCS:
        raise ValueError(
            f'Invalid track type: {type}. Choose from: {",".join(TRACK_FUNCS.keys())}'
        )
    click.echo(f"▶️ {green('starting')} {yellow('track')}: {blue(track)} on {yellow('audio_device')}: {blue(ad or 'default')} with {yellow('parent_pid')}: {blue(pid)}", err=True)
    return TRACK_FUNCS.get(type)(**options)


@click.command()
@seq_command_arg
@click.argument("base_config", type=click.File(), required=False)
@seq_opts
def cli(**kwargs):
    """
    Play a sequence of `chord`, `midi`, `note`, and/or `arp` tracks
    via yaml configuration.
    """
    run(**kwargs)
