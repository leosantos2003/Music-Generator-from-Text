from music_note import MusicNote

class MusicSequence:
    def __init__(self):
        self.notes: list[MusicNote] = []

    def add_note(self, note: MusicNote):
        self.notes.append(note)

    def extend(self, other_sequence: 'MusicSequence'):
        self.notes.extend(other_sequence.notes)

    def get_notes(self) -> list[MusicNote]:
        return self.notes