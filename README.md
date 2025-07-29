# Music Generator from Text

**INF01120 - Técnicas de Construção de Programas - UFRGS - 2025/1**

## About

This project is a Python application that converts free text into a musical sequence, which can be played in real time. Using a custom character mapping language, the user can control notes, rhythm, instruments, BPM, and other musical parameters directly through the graphical interface.

## Features

* **Real-Time Conversion:** Translates typed text into music instantly.

* **Intuitive Graphical Interface:** Interface built with `Tkinter` that allows for easy interaction, with controls for BPM, instrument, and play/stop buttons.

* **Rich Musical Language:** A comprehensive set of characters that control notes (A-G), rests, volume, octaves, BPM, and dynamic instrument selection.

* **Dynamic Control:** Change parameters such as BPM and instrumentation both through the interface and through commands in the text itself.

* **Music Management:** Save your compositions in `.txt` files and easily load them through a menu in the interface.

* **Modular Architecture:** The system was designed with a clear separation of responsibilities (GUI, Mapping, Playback, etc.), using abstract interfaces to ensure low coupling and high cohesion.

## How it works (Arquitecture)

The system is divided into well-defined modules, each with a unique responsibility. Communication between components is orchestrated by the graphical interface (`gui.py`), which uses the concrete implementations of the Mapper, Player, and Music Manager.

* **gui.py** (Interface): Captures user input and coordinates actions.

* **mapper.py** (Mapper): Converts the text string into a `MusicSequence` (list of notes and commands), applying the rules defined in `constants.py`.

* **player.py** (Player): Receives the `MusicSequence` and uses the `pygame.midi` library to play the sounds. Runs in a separate thread to avoid crashing the interface.

* **song_manager.py** (Manager): Handles reading and writing songs to `.txt` files.

* **Interfaces** (I*.py): Files like `Iplayer.py` and `Imapper.py` define contracts (abstract interfaces) that promote decoupling between components, facilitating testing and future extensions.

## How to run the project

To run this project, you will need:

* Python 3.0 or superior

* The `pygame` library for Python

Open the terminal at the root of the project and run the following command to install `pygame`:

```bash
py -m pip install pygame
```
After installation, you can run the project with the following command to start the graphical interface:

```bash
py main.py
```

## The musical language

| Category | Character(s) | Action |
|-------------|-------------|-------------|
| Musical Notes | A/a to G/g  | Plays the corresponding note (A, B, C, D, E, F, G). |
| Rhythm | Space | Inserts a rest. |
|  | BPM+ | Increases the BPM (Beats Per Minute) by 80 units. |
|  | ; | Assigns a random value to the BPM. |
| Dynamics | + | Doubles the current volume (up to 127). |
|  | - | Resets the volume to the default value (15). |
| Key and Octave | R+ | Increases one octave. |
|  | R- | Decreases one octave. |
|  | . | Increases one octave. If already at the maximum octave, it returns to the default. |
| Instruments | ! | Changes the instrument to Bandoneon (MIDI #24). |
|  | O/o/I/i/U/u | Repeats the previous note. If none, plays a Telephone sound (MIDI #124). |
|  | \n (new line) | Changes the instrument to a special one (Guitar Fret Noise, MIDI #27). |
|  | Odd Digits | Changes the instrument to Tubular Bells (MIDI #14). |
|  | Even Digits | Increases the current instrument by the digit value. |
|  | , | Changes the instrument to Agogô (MIDI #114). |
| Other | ? | Plays a random note between A and G. |
|  | Other Consonants | Repeat the last note played. If none, causes a rest. |

Inside the `saved_songs/` folder you will find some examples, like:

* `DoReMiFa.txt`
* `Halloween.txt`
* `Can't Stop.txt`

## Video Demo

working on it...

## License

Distributed under the MIT license. See `LICENSE.txt` for more information.

## Contact

Leonardo Santos - <leorsantos2003@gmail.com>
