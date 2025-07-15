import pygame
import pygame.midi
import threading
import time
from music_sequence import MusicSequence
from music_note import MusicNote
from Iplayer import IMusicPlayer
from constants import CONSTANTS
import random

class MusicPlayer(IMusicPlayer):
    def __init__(self):
        pygame.init()
        pygame.midi.init()
        self.port = pygame.midi.get_default_output_id()
        self.midi_out = pygame.midi.Output(self.port)
        self.instrument_id = CONSTANTS.DEFAULT_INSTRUMENT
        self.playing = False
        self.current_thread = None

    def set_instrument(self, instrument_id: int):
        self.instrument_id = instrument_id
        self.midi_out.set_instrument(self.instrument_id, CONSTANTS.DEFAULT_CHANNEL)
    
    def play(self, sequence: MusicSequence, bpm: int):
        if self.playing:
            self.stop()
        self.current_thread = threading.Thread(
            target=self.__play_sequence,
            args=(sequence, bpm),
            daemon=True
        )
        self.current_thread.start()

    def stop(self):
        self.playing = False

    def close(self):
        self.stop()
        self.midi_out.close()
        pygame.midi.quit()
        pygame.quit()

    def __play_sequence(self, sequence:MusicSequence, bpm: int):
        self.playing = True
        beat_duration = CONSTANTS.SECONDS_IN_MINUTE / bpm
        for note in sequence.get_notes():
            if not self.playing:
                break

            if self.__is_note_special_command(note.get_pitch()):
                match (note.get_pitch()):
                    case CONSTANTS.SILENCE_OR_PAUSE_CODE:
                        time.sleep(note.duration * beat_duration),
                    case CONSTANTS.INSTRUMENT_CHANGE_CODE:
                        self.__change_instrument(note.velocity),
                    case CONSTANTS.BPM_INCREASE_CODE:
                        bpm = min(bpm + CONSTANTS.BPM_INCREASE_VALUE, CONSTANTS.MAX_BPM)
                        beat_duration = CONSTANTS.SECONDS_IN_MINUTE / bpm
                    case CONSTANTS.BPM_RANDOM_CODE:
                        bpm = random.randint(CONSTANTS.MIN_BPM, CONSTANTS.MAX_BPM)
                        beat_duration = CONSTANTS.SECONDS_IN_MINUTE / bpm
            else:
                self.__play_note(note, beat_duration)
        self.playing = False
    
    def __is_note_special_command(self, pitch: int) -> bool:
        return pitch < 0

    def __change_instrument(self, instrument_id: int):
        self.instrument_id = instrument_id
        self.midi_out.set_instrument(self.instrument_id, CONSTANTS.DEFAULT_CHANNEL)

    def __play_note(self, note: MusicNote, beat_duration: float):
        self.midi_out.note_on(note.get_pitch(), note.velocity, CONSTANTS.DEFAULT_CHANNEL)
        time.sleep(note.duration * beat_duration)
        self.midi_out.note_off(note.get_pitch(), note.velocity, CONSTANTS.DEFAULT_CHANNEL)