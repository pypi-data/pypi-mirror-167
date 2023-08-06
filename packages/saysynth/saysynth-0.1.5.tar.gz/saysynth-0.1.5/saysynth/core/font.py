"""
The Font class creates a list of `Notes` within a
scale and writes them to separate files. This
makes them easy to import into samplers or DAWs.
"""
import os

from midi_utils import midi_scale, midi_to_note, note_to_midi

from .note import Note


class Font(object):
    def __init__(self, **kwargs):
        # add note type to simplify function call
        kwargs["type"] = "note"
        self.scale = midi_scale(
            key=kwargs["key"],
            scale=kwargs["scale"],
            min_note=note_to_midi(kwargs["scale_start_at"]),
            max_note=note_to_midi(kwargs["scale_end_at"]),
        )
        self._note_options = kwargs

    def _get_kwargs(self, midi, kwargs) -> dict:
        kw = dict(self._note_options)
        kw["type"] = "note"
        kw["midi"] = midi
        kw["note"] = midi_to_note(midi)
        kw.update(kwargs)
        return kw

    def play(self, **kwargs) -> None:
        try:
            os.makedirs(kwargs['output_dir'])
        except FileExistsError:
            pass
        # generate files for each note in the scale
        for midi in self.scale:
            kwargs = self._get_kwargs(midi, kwargs)

            # generate audio output file name
            filepath = (
                f"{kwargs['voice'].lower()}-{kwargs['rate']}-"
                f"{kwargs['note']}-{midi:02d}.{kwargs['format']}"
            )
            audio_output_file = os.path.join(
                kwargs["output_dir"],
                filepath,
            )
            # generate input file of text
            note = Note(**kwargs)
            note.play(
                voice=kwargs["voice"],
                rate=kwargs["rate"],
                audio_output_file=audio_output_file,
                wait_for_process=True
            )
            if not os.path.exists(audio_output_file):
                raise RuntimeError(
                    f"File {audio_output_file} was not successfully created"
                )
