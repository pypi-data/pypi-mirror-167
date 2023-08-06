"""
Print the current version of `saysynth` to the console.
"""
import click

from saysynth.version import VERSION


@click.command()
def cli():
    """
    Print the current version of `saysynth` to the console.
    """
    click.echo(f"saysynth (sy) version {VERSION}", err=True)
