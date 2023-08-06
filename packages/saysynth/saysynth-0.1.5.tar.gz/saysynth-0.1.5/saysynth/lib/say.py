"""
A Python-wrapper for Apple's [`say`](https://ss64.com/osx/say.html) command.
"""

import os
import subprocess
from typing import Any, Dict, List, Optional

from ..constants import (SAY_COLORS, SAY_DATA_TYPES, SAY_ENDIANESS,
                         SAY_EXECUTABLE, SAY_MAX_SAMPLE_RATE, SAY_SAMPLE_SIZES)
from ..utils import make_tempfile
from . import controller


def _gen_data_format_arg(
    endianess: str, data_type: str, sample_size: int, sample_rate: int
):
    """
    Generate a string to pass to --data-format
    """
    if endianess not in SAY_ENDIANESS:
        raise ValueError(
            "Invalid `endianess`. Choose from: LE (little endlian) or BE (big endian)"
        )
    if data_type not in SAY_DATA_TYPES:
        raise ValueError(
            "Invalid `data_type`. Choose from: F (float), I (integer), UI (unsigned integer)"
        )
    if sample_size not in SAY_SAMPLE_SIZES:
        raise ValueError(
            f'Invalid `sample_size`. Choose from: {", ".join(SAY_SAMPLE_SIZES)}'
        )

    # allow pass passing sample rate as small number (eg: 24 -> 24000)
    if sample_rate < 1000:
        sample_rate *= 1000

    # don't allow a sample rate greater than the maximum
    if sample_rate > SAY_MAX_SAMPLE_RATE:
        sample_rate = SAY_MAX_SAMPLE_RATE

    return f"{endianess}{data_type}{sample_size}@{int(sample_rate)}"


def _gen_interactive_arg(text_color: str = "white", bg_color: str = "black"):
    """
    Generate a string to pass to --interactive
    """
    if bg_color and not text_color:
        text_color = "white"  # default text color if only background is supplied
    if text_color not in SAY_COLORS:
        raise ValueError(f'Invalid `text_color`, choose from: {", ".join(SAY_COLORS)}')
    if bg_color not in SAY_COLORS:
        raise ValueError(f'Invalid `bg_color`, choose from: {", ".join(SAY_COLORS)}')
    return f"--interactive={text_color}/{bg_color}"


def cmd(
    input_text: Optional[str] = None,
    voice: Optional[str] = None,
    rate: Optional[int] = None,
    input_file: Optional[str] = None,
    audio_output_file: Optional[str] = None,
    service_name: Optional[str] = None,
    network_send: Optional[str] = None,
    audio_device: Optional[str] = None,
    stereo: bool = False,  # whether or not
    endianness: str = "LE",  # LE/BE
    data_type: str = "F",  # F/I/U
    sample_size: Optional[int] = 32,
    sample_rate: Optional[int] = 22050,
    quality: int = 127,
    progress: bool = False,
    interactive: bool = False,
    text_color: Optional[str] = None,
    bg_color: Optional[str] = None,
    executable: str = SAY_EXECUTABLE,
    **kwargs,
) -> List:
    """
    A python wrapper around the say command.

    Args:
        input_text: The text to speak
        voice: Specify the voice to be used. Default is the voice selected in System Preferences.
               To obtain a list of voices installed in the system, specify "?" as the voice name.
        rate:  Speech rate to be used, in words per minute.
        input_file:  Specify a file to be spoken. If file is - or neither this parameter nor a message is specified, read from standard input.
        audio_output_file: Specify the path for an audio file to be written.
                           AIFF is the default and should be supported for most voices, but some
        voices support many more file formats.
        service_name:  Specify a service name (default "AUNetSend")
        network_send: Specify an IP and port to be used for redirecting the speech output through AUNetSend.
        audio_device: Specify, by ID or name prefix, an audio device to be used to play the audio.
                      To obtain a list of audio output devices, specify "?" as the device name.
        stereo: Whether or not to output a stereo signal
        endianness: str = "LE",  # LE/BE
        data_type: str = "F",  # F/I/U
        sample_size: One of 8, 16, 24, 32, 64.
        sample_rate: Optional[int] = 22050,
        quality: The audio converter quality level between 0 (lowest) and 127 (highest).
        progress: Display a progress meter during synthesis.
        interactive: Print the text line by line during synthesis, highlighting words as they are spoken.
                     Markup can be one of
                     * A terminfo capability as described in terminfo(5), e.g. bold, smul, setaf 1.
                     * A color name, one of black, red, green, yellow, blue, magenta, cyan, or white.
                     * A foreground and background color from the above list, separated by a slash, e.g. green/black. If the foreground color
                       is omitted, only the background color is set.
                     * If markup is not specified, it defaults to smso, i.e. reverse video.
                     * If the input is a TTY, text is spoken line by line, and the output file, if specified, will only contain audio for the last line
                       of the input.  Otherwise, text is spoken all at once.
        text_color: A color name, one of black, red, green, yellow, blue, magenta, cyan, or white.
        bg_color: A color name, one of black, red, green, yellow, blue, magenta, cyan, or white.
        executable: The path to the `say` executable (default '/usr/bin/say'

    """  # noqa: E501
    if not input_text and not input_file:
        raise ValueError("Must provide `input_text` or `input_file`")

    # override text if input file is provided
    if input_file:
        # verify that input file exists
        if not os.path.exists(input_file):
            raise ValueError("`input_file`: {input_file} does not exist!")

    # verify quality
    if quality < 0 or quality > 127:
        raise ValueError("`quality` must be between 0 and 127")

    # construct base command
    cmd = [executable]
    if input_text:
        cmd.append(input_text)
    elif input_file:
        cmd.extend(["-f", input_file])
    if voice:
        cmd.extend(["-v", voice])
    if rate:
        cmd.extend(["-r", rate])

    if audio_output_file:
        # verify file_format:
        is_wave = audio_output_file.lower().endswith(".wav")
        is_aiff = audio_output_file.lower().endswith(".aiff")
        if not (is_wave or is_aiff):
            raise ValueError("`audio_output_file` must be of type .wav or .aiff")
        cmd.extend(["--file-format", f'{"WAVE" if is_wave else "AIFF"}'])
        cmd.extend(["-o", audio_output_file])
        # # # always specify data format with output file
        # data_format = _gen_data_format_arg(
        #   endianness, data_type, sample_size, sample_rate
        # )
        # cmd.append(
        #     f"--data-format={data_format}"
        # )
        if stereo:
            cmd.append("--channels=2")
    else:
        cmd.append(f"--quality={quality}")
        # handle network output if output file is not specified
        if service_name:
            cmd.extend(["-n", service_name])
        if network_send:
            cmd.extend(f"--network-send={network_send}")
        if audio_device:
            cmd.extend(["-a", audio_device])

    # progress bar
    if progress:
        cmd.append("--progress")

    # interactivity
    if interactive:
        cmd.append(_gen_interactive_arg(text_color, bg_color))
    return [str(a) for a in cmd]


def run(args: Optional[List] = None, **kwargs):
    """
    Execute a command given a list of arguments outputted by `cmd`
    or by supplying the kwargs that `cmd` accepts
    Args:
        args: A list of args generated by `cmd`
    """
    wait_for_process = kwargs.pop('wait_for_process', False)
    if not args:
        parent_pid = kwargs.pop("parent_pid", os.getpid())
        parent_pid_file = kwargs.pop("parent_pid_file", None)
        # write text as input file
        tempfile = None
        if kwargs.get("input_text"):
            text = kwargs.pop("input_text")
            # ALWAYS USE TEMPFILES FOR NOW.
            tempfile = make_tempfile()
            with open(tempfile, "w") as f:
                f.write(text)
            kwargs["input_file"] = tempfile
        args = cmd(**kwargs)
    process = None
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE)
        # register each process with the parent pid.
        controller.add_child_pid(process.pid, parent_pid, parent_pid_file)
        if wait_for_process:
            process.wait()
    except KeyboardInterrupt:
        pass


def _run_spawn(kwargs: Dict[str, Any]):
    """
    Utility for passing kwargs into `run` within `spawn`
    """
    return run(**kwargs)


def spawn(commands: List[Dict[str, Any]]):
    """
    Spawn multiple say processes in parallel by
    passing in a list of commands generated by `cmd`

    Args:
        commands: A list of command args generated by `cmd`
    """
    for command in commands:
        _run_spawn(command)
