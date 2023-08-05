"""
The `saysynth.cli.commands` module includes submodules containing the logic for each
saysynth command. Each submodule defines a `run` function which contains the logic
for executing the command and a `cli` function which includes the `click` decorators.
The `seq` submodule imports the `run` functions from a number of other submoudles
as it provides an interface for running multiple commands at once.a
"""
