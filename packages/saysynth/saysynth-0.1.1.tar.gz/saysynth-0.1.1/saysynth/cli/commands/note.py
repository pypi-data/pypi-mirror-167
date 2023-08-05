"""
Synthesize an individual note.
"""
import click
from midi_utils import note_to_midi

from saysynth import Note, controller
from saysynth.cli.options import (adsr_opts, duration_opts, output_file_opt,
                                  phoneme_opts, say_opts, segment_opts,
                                  show_volume_per_segment_opt, start_opts,
                                  text_opt, velocity_opts)


def run(**kwargs):
    note = Note(**kwargs)
    note.cli(**kwargs)


@click.command()
@click.argument("root", type=note_to_midi, default="A2")
@text_opt
@start_opts
@duration_opts
@phoneme_opts
@velocity_opts
@show_volume_per_segment_opt
@adsr_opts
@segment_opts
@output_file_opt
@say_opts
def cli(**kwargs):
    """
    Generate an individual note.
    """
    kwargs = controller.handle_cli_options('note', **kwargs)
    return run(**kwargs)
