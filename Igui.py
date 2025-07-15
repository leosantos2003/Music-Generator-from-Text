from abc import ABC, abstractmethod

class IMusicAppGUI(ABC):
    @abstractmethod
    def run(self):
        pass