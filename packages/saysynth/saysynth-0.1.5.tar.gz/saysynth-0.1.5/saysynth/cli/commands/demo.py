"""
Play a built-in demo.
"""

import os

import click
import pkg_resources

from saysynth.cli.commands.seq import run as run_sequence
from saysynth.cli.options import seq_command_arg, seq_opts

DEMO_DIR = pkg_resources.resource_filename("saysynth", "cli/commands/demos/")
DEMO_NAMES = [f.split("/")[-1].split(".yml")[0] for f in os.listdir(DEMO_DIR)]


def run(**kwargs):
    name = kwargs.pop("name")
    kwargs["base_config"] = open(os.path.join(DEMO_DIR, f"{name}.yml"), "r")
    run_sequence(**kwargs)


@click.command()
@seq_command_arg
@click.argument("name", type=click.Choice(DEMO_NAMES), default="fire")
@seq_opts
def cli(**kwargs):
    """
    Play a built-in demo.
    """
    return run(**kwargs)
