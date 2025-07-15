import tkinter as tk
from tkinter import ttk
from Igui import IMusicAppGUI
from Imapper import IMusicMapper
from Iplayer import IMusicPlayer
from Isong_manager import ISongManager
from mapper import MusicMapper
from player import MusicPlayer
from song_manager import SongManager
from constants import CONSTANTS
from text_pt_BR import TEXT

class MusicAppGUI(IMusicAppGUI):
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(TEXT.TITLE)

        self.mapper: IMusicMapper = MusicMapper()
        self.player: IMusicPlayer = MusicPlayer()
        self.song_manager: ISongManager = SongManager()

        self.instrument_var = tk.IntVar(value=CONSTANTS.DEFAULT_INSTRUMENT)
        self.bpm_var = tk.IntVar(value=CONSTANTS.DEFAULT_BPM)
        self.text_var = tk.StringVar(value=CONSTANTS.DEFAULT_SONG)
        self.song_name_var = tk.StringVar(value=CONSTANTS.DEFAULT_SONG_NAME)

        self.__create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.__on_close)
    
    def run(self):
        self.root.mainloop()

    def __create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(frame, text=TEXT.TEXT_LABEL).grid(row=0, column=0, sticky=tk.W)
        text_entry = ttk.Entry(frame, textvariable=self.text_var, width=50)
        text_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame, text=TEXT.COMBOBOX_LABEL).grid(row=1, column=0, sticky=tk.W)
        combo = ttk.Combobox(frame, values=self.song_manager.get_saved_songs())
        combo.state(["readonly"])
        combo.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
        botao = ttk.Button(frame, text=TEXT.APPLY_BUTTON, command=lambda: self.__on_apply_click(combo.get()))
        botao.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame, text=TEXT.INSTRUMENT_LABEL).grid(row=3, column=0, sticky=tk.W)
        instrument_entry = ttk.Entry(frame, textvariable=self.instrument_var, width=10)
        instrument_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(frame, text=TEXT.BPM_LABEL).grid(row=4, column=0, sticky=tk.W)

        self.lbl_bpm_value = ttk.Label(frame, text=str(self.bpm_var.get()))
        self.lbl_bpm_value.grid(row=4, column=2, sticky=tk.W)

        bpm_scale = ttk.Scale(
            frame, from_=CONSTANTS.MIN_BPM, to=CONSTANTS.MAX_BPM,
            orient=tk.HORIZONTAL,
            variable=self.bpm_var,
            command=self.__on_bpm_scale
        )
        bpm_scale.grid(row=4, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=5, column=0, columnspan=3, pady=10)
        ttk.Button(btn_frame, text=TEXT.PLAY_BUTTON, command=self.__on_play).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text=TEXT.STOP_BUTTON, command=self.__on_stop).pack(side=tk.LEFT, padx=5)

        ttk.Label(frame, text=TEXT.SONG_NAME_LABEL).grid(row=6, column=0, sticky=tk.W)
        song_name_entry = ttk.Entry(frame, textvariable=self.song_name_var, width=30)
        song_name_entry.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)
        botao = ttk.Button(frame, text=TEXT.SAVE_BUTTON, command=lambda: self.__on_save_click(combo))
        botao.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)


    def __on_bpm_scale(self, val):
        self.bpm_var.set(int(float(val)))
        self.lbl_bpm_value.config(text=str(self.bpm_var.get()))

    def __on_play(self):
        self.player.set_instrument(self.instrument_var.get())

        self.mapper.reset_state(self.instrument_var.get())

        sequence = self.mapper.text_to_sequence(self.text_var.get())
        self.player.play(sequence, self.bpm_var.get())

    def __on_stop(self):
        self.player.stop()

    def __on_close(self):
        self.player.close()
        self.root.destroy()

    def __on_apply_click(self, option):
        self.text_var.set(self.song_manager.load_song(option))
    
    def __on_save_click(self, combobox):
        self.song_manager.save_song(self.text_var.get(), self.song_name_var.get())
        self.__update_combobox_values(combobox)
    
    def __update_combobox_values(self, combobox):
        combobox["values"] = self.song_manager.get_saved_songs()