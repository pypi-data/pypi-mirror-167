"""
Utilities for registering processes as files under `~/.saysynth/pid` so they can be dynamically stopped.
"""
import os
import signal
from pathlib import Path
from typing import List, Optional

import click

# where to log pids of of sequences
# these will take the form of
# ~/.saysynth/pid/{seq}.{track}.{pid}
SEQUENCE_PID_LOG = os.path.expanduser("~/.saysynth/pid")


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
    pid: Optional[int] = None,
) -> List[Path]:
    """
    List pid file paths by seq, track, and/or pid
    """
    return Path(SEQUENCE_PID_LOG).glob(
        f'{seq or "*"}.{track or "*"}.{ad or "*"}.{pid or "*"}'
    )


def add_parent_pid(seq: str, track: str, ad: str, pid: int) -> None:
    """
    Associate a pid with a track wihin a sequence.
    """
    ensure_pid_log()
    Path(f"{SEQUENCE_PID_LOG}/{seq}.{track}.{ad}.{pid}").touch()


def rm_parent_pid(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> None:
    """
    Remove pid log files for a seq and/or track
    """
    for path in _list_pid_file_paths(seq, track, ad, parent_pid):
        path.unlink()


def add_child_pid(child_pid: int, parent_pid: int) -> None:
    """
    Add a child pid to a parent_pid
    """
    paths = _list_pid_file_paths(pid=parent_pid)
    for path in paths:
        _append_pid_file(path, child_pid)


def rm_child_pid(child_pid: int, parent_pid: int) -> None:
    """
    Remove a child pid from a parent_pid
    """
    paths = _list_pid_file_paths(pid=parent_pid)
    for path in paths:
        pids = set(_read_pid_file(path))
        pids.remove(child_pid)
        _write_pid_file(path, pids)


def lookup_parent_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> List[int]:
    """
    Lookup all of the parent pids for a seq and/or track
    """
    return [
        int(str(path).split(".")[-1]) for path in _list_pid_file_paths(seq, track, ad, parent_pid)
    ]


def lookup_child_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None,
    parent_pid: Optional[int] = None,
) -> List[int]:
    """
    Lookup the child pids for a seq and/or track
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
    Lookup all pids for a sequence / track
    """
    return lookup_parent_pids(seq, track, ad, parent_pid) + lookup_child_pids(seq, track, ad, parent_pid)


def stop_child_pids(
    seq: Optional[str] = None, track: Optional[str] = None, ad: Optional[str] = None, parent_pid: Optional[int] = None,
) -> None:
    """
    Stop all the child pids of a parent.
    """
    pids = lookup_child_pids(seq, track, ad, parent_pid)
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            # remove the pid log file
            for path in _list_pid_file_paths(pid=pid):
                path.unlink()
    rm_parent_pid(seq, track, ad, parent_pid)


def handle_cli_options(command, **kwargs) -> dict:
    parent_pid = os.getpid()
    add_parent_pid('__sy__', command, kwargs.get('audio_device'), parent_pid)
    click.echo(f'Starting {command} with pid: {parent_pid}')
    kwargs['parent_pid'] = parent_pid
    return kwargs
