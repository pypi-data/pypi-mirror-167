"""
Stop all currently running `say` processes.
"""
import click

from saysynth import controller


@click.command()
@click.argument("pid")
def cli(**kwargs):
    """
    Stop currently running `saysynth` processes by passing in the parent `pid`
    or `all` for all processes.
    """
    parent_pid = '*' if kwargs['pid'] == 'all' else kwargs['pid']
    controller.stop_child_pids(parent_pid=parent_pid)
    controller.rm_parent_pid(parent_pid=parent_pid)
