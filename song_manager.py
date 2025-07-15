from Isong_manager import ISongManager
import os
from constants import CONSTANTS

class SongManager(ISongManager):
    def get_saved_songs(self) -> list[str]:
        folder = CONSTANTS.SAVED_SONGS_FOLDER_PATH
        files = [os.path.splitext(f)[0] for f in os.listdir(folder)
                if f.endswith(CONSTANTS.TXT_EXTENSION) and os.path.isfile(os.path.join(folder, f))]
        return files

    def load_song(self, file_name: str) -> str:
        with open(f"{CONSTANTS.SAVED_SONGS_FOLDER_PATH}/{file_name}{CONSTANTS.TXT_EXTENSION}", "r", encoding="utf-8") as file:
            text = file.read()
        return text
    
    def save_song(self, stream: str, file_name: str):
        if self.__is_stream_not_blank(stream) and self.__is_file_name_not_blank(file_name):
            with open(f"{CONSTANTS.SAVED_SONGS_FOLDER_PATH}/{file_name}{CONSTANTS.TXT_EXTENSION}", "w", encoding="utf-8") as file:
                file.write(stream)

    def __is_stream_not_blank(self, stream: str) -> bool:
        return stream != ''
    
    def __is_file_name_not_blank(self, file_name: str) -> bool:
        return file_name != ''