import os

import click

from saysynth.lib.controller import rm_parent_pid

@click.command()
def cli(**kwargs):
    os.system('pgrep say | xargs kill -9')
    rm_parent_pid()