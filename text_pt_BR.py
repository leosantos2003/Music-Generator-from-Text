from types import MappingProxyType

class Text:
    TITLE = "Gerador de Música a partir de Texto"
    TEXT_LABEL = "Texto:"
    INSTRUMENT_LABEL = "Instrumento (GM ID):"
    BPM_LABEL = "BPM:"
    PLAY_BUTTON = "Tocar"
    STOP_BUTTON = "Parar"
    COMBOBOX_LABEL = "Escolher Música:"
    APPLY_BUTTON = "Aplicar"
    SONG_NAME_LABEL = "Nome da Música:"
    SAVE_BUTTON = "Salvar"

    def __setattr__(self, name, value):
        raise AttributeError("Cannot modify constant values")

TEXT = Text()