from abc import ABC, abstractmethod
from music_sequence import MusicSequence

class IMusicPlayer(ABC):
    @abstractmethod    
    def set_instrument(self, instrument_id: int):
        pass

    @abstractmethod    
    def play(self, sequence: MusicSequence, bpm: int):
        pass

    @abstractmethod    
    def stop(self):
        pass

    @abstractmethod    
    def close(self):
        pass