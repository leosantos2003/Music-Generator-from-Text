from music_note import MusicNote
from music_sequence import MusicSequence
from Imapper import IMusicMapper
from constants import CONSTANTS
from instrument import Instrument
import random

class MusicMapper(IMusicMapper):
    def __init__(self, current_instrument=CONSTANTS.DEFAULT_INSTRUMENT):
        self.reset_state(current_instrument)
    
    def reset_state(self, current_instrument=CONSTANTS.DEFAULT_INSTRUMENT):
        self.current_volume = CONSTANTS.DEFAULT_VOLUME
        self.note_duration = CONSTANTS.NOTE_DURATION
        self.current_octave = CONSTANTS.DEFAULT_OCTAVE
        self.current_instrument = current_instrument

    def text_to_sequence(self, text: str) -> MusicSequence:
        sequence = MusicSequence()
        last_char = None  # Para armazenar o último caracter lido

        i = 0
        while (i < text.__len__()):
            char = text[i]

            # Comando: Aumentar Oitava
            if self.__is_str_command(text, i, CONSTANTS.OCTAVE_INCREASE_STR):
                self.current_octave = min(self.current_octave + 1, CONSTANTS.MAX_OCTAVE)
                i += CONSTANTS.OCTAVE_INCREASE_STR.__len__() - 1
                
            # Comando: Diminuir Oitava
            elif self.__is_str_command(text, i, CONSTANTS.OCTAVE_DECREASE_STR):
                self.current_octave = max(self.current_octave - 1, CONSTANTS.DEFAULT_OCTAVE)
                i += CONSTANTS.OCTAVE_DECREASE_STR.__len__() - 1
            
            # Comando: Aumentar BPM
            elif self.__is_str_command(text, i, CONSTANTS.BPM_INCREASE_STR):
                self.__add_bpm_increase_to_sequence(sequence)
                i += CONSTANTS.BPM_INCREASE_STR.__len__() - 1
            
            # Comando: BPM Aleatório
            elif char == CONSTANTS.RANDOM_BPM_CHAR:
                self.__add_random_bpm_to_sequence(sequence)
            
            # Comando: Aumentar ou Resetar Oitava
            elif char == CONSTANTS.OCTAVE_INCREASE_OR_RESET_CHAR:
                if self.current_octave < CONSTANTS.MAX_OCTAVE:
                    self.current_octave += 1
                else:
                    self.current_octave = CONSTANTS.DEFAULT_OCTAVE

            # Comando: Aumentar Volume
            elif char == CONSTANTS.VOLUME_INCREASE_CHAR:
                self.current_volume = min(self.current_volume * 2, CONSTANTS.MAX_VOLUME)

            # Comando: Resetar Volume
            elif char == CONSTANTS.VOLUME_RESET_CHAR:
                self.current_volume = CONSTANTS.DEFAULT_VOLUME

            # Comando: Instrumento -> Especial
            elif char == CONSTANTS.SPECIAL_INSTRUMENT_CHAR:
                self.__add_instrument_change_to_sequence(sequence, Instrument.SPECIAL.value)

            # Comando: Instrumento -> Bandoneon
            elif char == CONSTANTS.BANDONEON_CHAR:
                self.__add_instrument_change_to_sequence(sequence, Instrument.BANDONEON.value)

            # Comando: Instrumento -> Tubular Bells
            elif self.__is_char_odd_number(char):
                self.__add_instrument_change_to_sequence(sequence, Instrument.TUBULAR_BELLS.value)
            
            # Comando: Instrumento -> Agogô
            elif char == CONSTANTS.AGOGO_CHAR:
                self.__add_instrument_change_to_sequence(sequence, Instrument.AGOGO.value)

            # Comando: Instrumento -> Instrumento + Input
            elif self.__is_char_even_number(char):
                new_instrument = min(self.current_instrument + int(char), CONSTANTS.MAX_INSTRUMENT)
                self.__add_instrument_change_to_sequence(sequence, new_instrument)

            # Comando: Repetir Nota ou Telefone
            elif char in CONSTANTS.REPEAT_OR_PHONE_CHARS:
                if last_char in CONSTANTS.NOTE_CHARS:
                    sequence.add_note(MusicNote(self.__get_pitch_from_note_char(last_char), self.current_volume, self.note_duration))
                else:
                    self.__add_single_telephone_note_to_sequence(sequence)

            # Comando: Nota Pausa
            elif char in CONSTANTS.PAUSE_CHAR:
                self.__add_pause_to_sequence(sequence)

            # Comando: Nota Musical
            elif char in CONSTANTS.NOTE_CHARS:
                sequence.add_note(MusicNote(self.__get_pitch_from_note_char(char), self.current_volume, self.note_duration))
            
            # Comando: Nota Aleatória
            elif char == CONSTANTS.RANDOM_NOTE_CHAR:
                sequence.add_note(MusicNote(self.__get_pitch_from_note_char(self.__get_random_note_char()), self.current_volume, self.note_duration))
            
            # Comando: Repetir Nota ou Pausar
            # Consoante não nota/qualquer outro caracter (possuem a mesma regra)
            else:
                if last_char in CONSTANTS.NOTE_CHARS:
                    sequence.add_note(MusicNote(self.__get_pitch_from_note_char(last_char), self.current_volume, self.note_duration))
                else:
                    self.__add_pause_to_sequence(sequence)

            last_char = char
            i += 1
        return sequence

    def __is_str_command(self, text: str, index: int, command: str) -> bool:    # Checks for a command composed by more than 1 character, like 'BPM+' or 'R-'
        return index + command.__len__() <= text.__len__() and text[index : index + command.__len__()] == command

    def __is_char_odd_number(self, char: str) -> bool:
        return (len(char) == 1 and char.isdigit() and int(char) % 2 == 1)

    def __is_char_even_number(self, char: str) -> bool:
        return len(char) == 1 and char.isdigit() and int(char) % 2 == 0
    
    def __add_instrument_change_to_sequence(self, sequence: MusicSequence, instrument: int):
        sequence.add_note(MusicNote(pitch=CONSTANTS.INSTRUMENT_CHANGE_CODE, velocity=instrument, duration=0))
        self.current_instrument = instrument
    
    def __add_pause_to_sequence(self, sequence: MusicSequence):
        sequence.add_note(MusicNote(pitch=CONSTANTS.SILENCE_OR_PAUSE_CODE, velocity=0, duration=self.note_duration))

    def __add_bpm_increase_to_sequence(self, sequence: MusicSequence):
        sequence.add_note(MusicNote(pitch=CONSTANTS.BPM_INCREASE_CODE, velocity=0, duration=self.note_duration))
    
    def __add_random_bpm_to_sequence(self, sequence: MusicSequence):
        sequence.add_note(MusicNote(pitch=CONSTANTS.BPM_RANDOM_CODE, velocity=0, duration=self.note_duration))

    def __get_pitch_from_note_char(self, char) -> int:
        return CONSTANTS.NOTES[str.upper(char)] + (CONSTANTS.NOTES_IN_OCTAVE * self.current_octave)
    
    def __get_random_note_char(self) -> str:
        return CONSTANTS.NOTE_CHARS[random.randint(0, CONSTANTS.NOTE_CHARS.__len__() - 1)]
    
    def __add_single_telephone_note_to_sequence(self, sequence: MusicSequence):
        sequence.add_note(MusicNote(pitch=CONSTANTS.INSTRUMENT_CHANGE_CODE, velocity=Instrument.TELEPHONE.value, duration=0))
        sequence.add_note(MusicNote(self.__get_pitch_from_note_char(self.__get_random_note_char()), self.current_volume, self.note_duration))
        sequence.add_note(MusicNote(pitch=CONSTANTS.INSTRUMENT_CHANGE_CODE, velocity=self.current_instrument, duration=0))
