"""
List all currently running `saysynth` processes.
"""
import click

from saysynth import controller
from saysynth.cli.colors import blue, green, red, yellow


def run(**kwargs):
    pids = controller.list_pids()
    if not len(pids):
        click.echo(red("There are no active processes!"))
        return
    last_seq = None
    for p in pids:
        seq = p["seq"]
        if last_seq != seq:
            click.echo(r"-" * 70, err=True)
            click.echo(f"{red('sequence')}: {green(p['seq'])}")
            click.echo(r"-" * 70, err=True)
        click.echo(
            f"➡️ {yellow('track')}: {blue(p['track'])} {yellow('audio_device')}: {blue(p['ad'])} {yellow('parent_pid')}: {blue(p['parent_pid'])} {yellow('child_pids')}: {blue(len(p['child_pids']))}"
        )
        last_seq = seq


@click.command()
def cli(**kwargs):
    """
    List all currently running `saysynth` processes.
    """
    run(**kwargs)
