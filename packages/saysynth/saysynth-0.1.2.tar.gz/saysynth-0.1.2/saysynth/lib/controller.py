"""
Utilities for registering processes as files under `~/.saysynth/pid` so they can be dynamically stopped.
"""
import os
import signal
from pathlib import Path
from typing import List, Optional

import click

SEQUENCE_PID_LOG = os.path.expanduser("~/.saysynth/pid")
"""
Where to log child pids of parent processes.
These will take the form of `~/.saysynth/pid/{seq}.{track}.{audio_device}.{parent_pid}`
"""


def _read_pid_file(path: str) -> List[int]:
    with open(path, "r") as f:
        return list([int(line.strip()) for line in f.readlines()])


def _append_pid_file(path: str, pid: int) -> None:
    with open(path, "a") as f:
        f.write(str(pid) + "\n")


def _write_pid_file(path, pids) -> None:
    with open(path, "w") as f:
        f.write("\n".join([str(p) for p in pids]))


def ensure_pid_log() -> None:
    if not os.path.exists(SEQUENCE_PID_LOG):
        os.makedirs(SEQUENCE_PID_LOG)


def _list_pid_file_paths(
    seq: Optional[str] = None,
    track: Optional[str] = None,
    ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> List[Path]:
    """
    List pid file paths by seq, track, and/or pid.

    Args:
        seq: An optional sequence name to filter file paths by
        track: An optional track name to filter file paths by
        ad: An optional audio device to filter file paths by
        parent_pid: An optional parent_pid to filter file paths by
    """
    return Path(SEQUENCE_PID_LOG).glob(
        f'{seq or "*"}.{track or "*"}.{ad or "*"}.{parent_pid or "*"}'
    )


def add_parent_pid(seq: str, track: str, ad: str, parent_pid: int) -> None:
    """
    Associate a pid with a track wihin a sequence.

    Args:
        seq: An optional sequence name to associate with the parent pid
        track: An optional track name to associate with the parent pid
        ad: An optional audio device to associate with the parent pid
        parent_pid: The parent pid
    """
    ensure_pid_log()
    path = f"{SEQUENCE_PID_LOG}/{seq}.{track}.{ad}.{parent_pid}"
    Path(path).touch()
    return path


def rm_parent_pid(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> None:
    """
    Remove pid log files for a seq and/or track

    Args:
        seq: An optional sequence name to remove pids by
        track: An optional track name to remove pids by
        ad: An optional audio device to remove pids by
        parent_pid: An optional parent_pid to remove pids by
    """
    for path in _list_pid_file_paths(seq, track, ad, parent_pid):
        path.unlink()


def add_child_pid(child_pid: int, parent_pid: int, parent_pid_file: Optional[str]) -> None:
    """
    Add a child pid to a parent_pid.

    Args:
        child_pid: The child process to register with the parent.
        parent_pid: The parent pid.
    """
    if parent_pid_file:
        paths = [parent_pid_file]
    else:
        paths = _list_pid_file_paths(parent_pid=parent_pid)
    for path in paths:
        _append_pid_file(path, child_pid)


def rm_child_pid(child_pid: int, parent_pid: int) -> None:
    """
    Remove a child pid from a parent_pid.

    Args:
        child_pid: The child process to dergisister from the parent.
        parent_pid: The parent pid.
    """
    paths = _list_pid_file_paths(parent_pid=parent_pid)
    for path in paths:
        pids = set(_read_pid_file(path))
        pids.remove(child_pid)
        _write_pid_file(path, pids)


def lookup_parent_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> List[int]:
    """
    Lookup all of the parent pids for a seq and/or track.

    Args:
        seq: An optional sequence name to filter parent pids by
        track: An optional track name to filter parent pids by
        ad: An optional audio device to filter parent pids by
        parent_pid: An optional parent_pid to filter parent pids by
    """
    return [
        int(str(path).split(".")[-1]) for path in _list_pid_file_paths(seq, track, ad, parent_pid)
    ]


def lookup_child_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> List[int]:
    """
    Lookup the child pids for a seq and/or track.

    Args:
        seq: An optional sequence name to filter child pids by
        track: An optional track name to filter child pids by
        ad: An optional audio device to filter child pids by
        parent_pid: An optional parent_pid to filter child pids by
    """
    pids = []
    for path in _list_pid_file_paths(seq, track, ad, parent_pid):
        pids.extend(_read_pid_file(path))
    return list(set(pids))


def lookup_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> None:
    """
    Lookup all pids for a sequence / track.

    Args:
        seq: An optional sequence name to filter pids by
        track: An optional track name to filter pids by
        ad: An optional audio device to filter pids by
        parent_pid: An optional parent_pid to filter pids by
    """
    return lookup_parent_pids(seq, track, ad, parent_pid) + lookup_child_pids(seq, track, ad, parent_pid)


def stop_child_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None, parent_pid: Optional[int] = None,
) -> None:
    """
    Stop all the child pids of a parent.

    Args:
        seq: An optional sequence name to stop child pids by
        track: An optional track name to stop child pids by
        ad: An optional audio device to stop child pids by
        parent_pid: An optional parent_pid to stop child pids by
    """
    pids = lookup_child_pids(seq, track, ad, parent_pid)
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            # remove the pid log file
            for path in _list_pid_file_paths(parent_pid=pid):
                path.unlink()
    rm_parent_pid(seq, track, ad, parent_pid)


def handle_cli_options(command, **kwargs) -> dict:
    """
    Initialize controller and set cli options.

    Args:
        command: The name of the cli command (eg: `chord`)
    """
    parent_pid = os.getpid()
    add_parent_pid('__sy__', command, kwargs.get('audio_device'), parent_pid)
    click.echo(f'Starting {command} with pid: {parent_pid}', err=True)
    kwargs['parent_pid'] = parent_pid
    return kwargs
