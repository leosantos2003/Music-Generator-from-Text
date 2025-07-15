from types import MappingProxyType

class Constants:
    NOTE_CHARS = 'aAbBcCdDeEfFgG'
    PAUSE_CHAR = ' '
    NOTES = MappingProxyType ({
        'A': 45,  # Lá
        'B': 47,  # Si
        'C': 36,  # Dó
        'D': 38,  # Ré
        'E': 40,  # Mi
        'F': 41,  # Fá
        'G': 43,  # Sol
    })
    SILENCE_OR_PAUSE_CODE = -1
    INSTRUMENT_CHANGE_CODE = -2
    BPM_INCREASE_CODE = -3
    BPM_RANDOM_CODE = -4
    BANDONEON_CHAR = '!'
    AGOGO_CHAR = ','
    VOLUME_INCREASE_CHAR = '+'
    VOLUME_RESET_CHAR = '-'
    REPEAT_OR_PHONE_CHARS = 'OoIiUu'
    OCTAVE_INCREASE_STR = 'R+'
    OCTAVE_DECREASE_STR = 'R-'
    OCTAVE_INCREASE_OR_RESET_CHAR = '.'
    RANDOM_NOTE_CHAR = '?'
    SPECIAL_INSTRUMENT_CHAR = '\n'
    BPM_INCREASE_STR = 'BPM+'
    RANDOM_BPM_CHAR = ';'
    SAVED_SONGS_FOLDER_PATH = './saved_songs'
    TXT_EXTENSION = '.txt'
    DEFAULT_VOLUME = 15
    MAX_VOLUME = 127
    NOTE_DURATION = 1.0
    DEFAULT_INSTRUMENT = 0
    MAX_INSTRUMENT = 127
    NOTES_IN_OCTAVE = 12
    DEFAULT_OCTAVE = 0
    MAX_OCTAVE = 5
    SECONDS_IN_MINUTE = 60.0
    DEFAULT_CHANNEL = 0
    DEFAULT_SONG = ""
    DEFAULT_SONG_NAME = ""
    MIN_BPM = 60
    DEFAULT_BPM = 120
    MAX_BPM = 360
    BPM_INCREASE_VALUE = 80

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify constant values")

CONSTANTS = Constants()