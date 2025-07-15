from abc import ABC, abstractmethod
from music_sequence import MusicSequence

class IMusicMapper(ABC):
    @abstractmethod    
    def reset_state(self, current_instrument: int):
        pass
    
    @abstractmethod    
    def text_to_sequence(self, text: str) -> MusicSequence:
        pass