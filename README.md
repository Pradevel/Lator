# Lator

Lator is a simple GUI-based application that allows you to record audio, recognize the speech in English, translate it to Hindi, and then convert the translated text into speech. 

The application is built using Python, with `Tkinter` for the GUI, and leverages the power of `Vosk` for speech recognition, `GoogleTranslator` for translation, and `gTTS` for text-to-speech conversion.

## Features

- **Audio Recording**: Record audio using your microphone.
- **Speech Recognition**: Recognize English speech from the recorded audio.
- **Translation**: Translate recognized English text to Hindi.
- **Text-to-Speech**: Convert the translated Hindi text into speech and save it as an MP3 file.

## Installation

### Prerequisites

Make sure you have Python installed. You can install the required dependencies using `pip`:

```bash
pip install pyaudio vosk gtts deep-translator
```
### Setting Up the Vosk Model
- Download the Vosk model and place it in your project directory. You can download the model from Vosk Models.
- For this project, the vosk-model-small-en-us-0.15 model is used.

## Usage
### Run the Application:
    python main.py
### Interact with the GUI:
- Enter the duration for which you want to record audio.
- Click on "Record and Translate" to start recording.
- Once the recording is complete, the recognized text and its translation will be displayed.
- The translated text will be saved as speech in an MP3 file named output.mp3.
### Example
- Recording Duration: You can specify the length of the audio recording in seconds.
- Recognized Text: The text recognized from the audio will be shown in the GUI.
- Translated Text: The translation of the recognized text into Hindi will also be shown in the GUI.
- Output: The Hindi speech is saved as an MP3 file named output.mp3.
## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements.

## Acknowledgments
- Vosk Speech Recognition
- Google Translator
- gTTS (Google Text-to-Speech)
- Tkinter
## Contact
For any questions or feedback, please reach out to [Pradevel]("mailto:pratyushroy.whj@gmail.com").