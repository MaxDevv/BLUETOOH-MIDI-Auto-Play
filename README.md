# Bluetooth MIDI AutoPlayer

Bluetooth MIDI AutoPlayer is a background software that automatically connects to Bluetooth MIDI devices and synthesizes their audio using FluidSynth with velocity curves using mididings.

## Features

- Automatic connection to Bluetooth MIDI devices
- Audio synthesis using FluidSynth
- Velocity curves using mididings

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/MaxDevv/Bluetooth-MIDI-AutoPlayer.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Bluetooth-MIDI-AutoPlayer
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script to start the Bluetooth MIDI AutoPlayer:
```sh
python main.py
```

## License

This project is licensed under the GPL 3.0 License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any inquiries, please contact the repository owner.

## Running in the Background

To run Bluetooth MIDI AutoPlayer in the background using the Startup Applications function on Linux:

1. Open the Startup Applications Preferences from your application menu.
2. Click on "Add" to create a new startup program.
3. Set the name to "Bluetooth MIDI AutoPlayer".
4. Set the command to:
    ```sh
    /usr/bin/python3 /path/to/Bluetooth-MIDI-AutoPlayer/main.py
    ```
5. Optionally, add a comment for the startup program.
6. Click "Add" to save the new startup program.

This software is designed for Linux and has not been tested on other operating systems.

*This README was created with the assistance of AI.*