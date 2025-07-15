import tkinter as tk
from gui import MusicAppGUI
from Igui import IMusicAppGUI


def main():    
    root = tk.Tk()
    app: IMusicAppGUI = MusicAppGUI(root)
    app.run()

if __name__ == "__main__":
    main()

