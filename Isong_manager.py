from abc import ABC, abstractmethod

class ISongManager(ABC):
    @abstractmethod    
    def get_saved_songs(self) -> list[str]:
        pass

    @abstractmethod    
    def load_song(self, file_name: str) -> str:
        pass

    @abstractmethod    
    def save_song(self, stream: str, file_name: str):
        pass