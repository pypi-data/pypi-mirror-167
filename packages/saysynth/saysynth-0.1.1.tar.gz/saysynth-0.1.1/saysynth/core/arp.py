"""The Arp class enables melodic speech synthesis by mapping input text or phonemes onto a configurable arpeggiator.
"""
import random
from functools import cached_property
from typing import List, Optional, Union

from midi_utils import midi_arp

from .base import SayObject
from .lyrics import Lyrics
from .note import Note
from .segment import Segment


class Arp(SayObject):
    def __init__(
        self,
        text: Optional[str] = None,  # text to 'sing'
        notes: List[int] = [],  # arbitrary list of notes to arpeggiate
        root: str = "A3",  # root note of chord
        chord: str = "min6_9",  # chord name,
        inversions: List[int] = [],  # inversions list
        stack: int = 0,  # stack a chord up or down
        styles: List[str] = ["down"],
        octaves: List[int] = [0],  # a list of octaves to add to the notes (eg: [-1, 2])
        velocities: List[int] = [100],
        # a list of velocities to apply across notes,
        # velocities are retrieved using a modulo so
        # this can be any duration and will be applied
        # in order
        show_volume_per_note: int = 3,
        beat_bpm: float = 131.0,  # bpm to use when determining beat length
        beat_count: Union[float, int, str] = "1/16",  # count of one beat of the arp
        beat_time_sig: str = "4/4",  # time signature of arp
        beat_duration: Optional[float] = None,  # the time of the note in ms
        note_bpm: float = 131.0,  # bpm to use when determining note duration
        note_count: Union[
            float, int, str
        ] = "3/64",  # count of note legth (should be less than or equat to beat count)
        note_time_sig: str = "4/4",  # time signature of arp
        note_duration: Optional[float] = None,  # arbitrary duration of note in ms
        randomize_start: Optional[List[int]] = None,
        start_bpm: float = 131.0,  # bpm to use when determining the start of the arp and adds silence at the beginning
        start_count: Union[float, int, str] = 0,  # the start beat count
        start_time_sig: str = "4/4",  # time signature to use when determining start
        start_duration: Optional[
            float
        ] = None,  # the amount of silence to add at the beginning in ms
        duration_bpm: float = 131.0,  # bpm to use when determining note duration
        duration_count: Union[float, int, str] = "16",  # the duration beat count
        duration_time_sig: str = "4/4",  # time signature to use when determining duration
        duration: Optional[float] = None,  # the total duration of the pattern in ms
        loops: Optional[int] = None,
        **note_options,
    ):
        self.styles = styles

        if randomize_start:
            start_duration = random.choice(
                range(randomize_start[0], randomize_start[1] + 1)
            )

        self.sequence = midi_arp(
            notes=notes,
            root=root,
            chord=chord,
            inversions=inversions,
            stack=stack,
            octaves=octaves,
            styles=styles,
            velocities=velocities,
            beat_bpm=beat_bpm,
            beat_count=beat_count,
            beat_time_sig=beat_time_sig,
            beat_duration=beat_duration,
            note_bpm=note_bpm,
            note_count=note_count,
            note_time_sig=note_time_sig,
            note_duration=note_duration,
            start_bpm=start_bpm,
            start_count=start_count,
            start_time_sig=start_time_sig,
            start_duration=start_duration,
            duration_bpm=duration_bpm,
            duration_count=duration_count,
            duration_time_sig=duration_time_sig,
            duration=duration,
            loops=loops,
        )
        self.show_volume_per_note = show_volume_per_note
        self._note_options = note_options
        self.lyrics = None
        if text:
            self.lyrics = Lyrics(text)

    def _get_kwargs(self, index, **kwargs):
        """
        get kwargs + update with new ones
        used for mapping similar kwards over different notes
        """
        d = dict(self._note_options.items())
        d.update(kwargs)
        d["show_volume"] = index % self.show_volume_per_note == 0
        return d

    @cached_property
    def notes(self) -> List[Note]:
        """
        The generated list of `Note` in the Arp.
        """
        start_at_phoneme = 0
        _notes = []
        for i, note in enumerate(self.sequence):
            note_kwargs = self._get_kwargs(i, **note)
            if self.lyrics:
                # handle text / phoneme:
                phonemes = self.lyrics.get_phonemes(start_at=start_at_phoneme)
                if len(phonemes) == 0:
                    # TODO: Fix this hack.
                    start_at_phoneme = 0
                    phonemes = self.lyrics.get_phonemes(start_at=start_at_phoneme)
                note_kwargs["phoneme"] = phonemes
            note = Note(**note_kwargs)
            last_note_length = note.n_segments
            start_at_phoneme += last_note_length
            _notes.append(note)
        return _notes

    @cached_property
    def segments(self) -> List[Segment]:
        """
        The generated list of `Segment` in the Arp.
        """
        return [segment for note in self.notes for segment in note.segments]

    @cached_property
    def n_notes(self) -> int:
        """
        The number of Notes in the Arp.
        """
        return len(self.notes)

    @cached_property
    def n_segments(self) -> int:
        """
        The number of Segments in the Arp.
        """
        return sum([note.n_segments for note in self.notes])

    def to_text(self):
        """
        Render this Arp as Apple SpeechSynthesis DSL text.
        """
        return "\n".join([n.to_text() for n in self.notes])

    def __repr__(self):
        return f"<Arp {','.join(self.styles)}"
