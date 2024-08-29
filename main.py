import pyaudio
import wave
import json
from vosk import Model, KaldiRecognizer
from gtts import gTTS
from deep_translator import GoogleTranslator
import tkinter as tk
from tkinter import messagebox, filedialog


def record_audio(output_file, record_seconds=5, sample_rate=16000):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=1024)

    print("Recording...")
    frames = []
    for _ in range(0, int(sample_rate / 1024 * record_seconds)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()


def recognize_speech(audio_file):
    model = Model("vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)

    with wave.open(audio_file, "rb") as wf:
        recognizer.AcceptWaveform(wf.readframes(wf.getnframes()))
        result = recognizer.Result()

    text = json.loads(result).get('text', '')
    return text


def translate_to_hindi(text):
    translator = GoogleTranslator(source='en', target='hi')
    translation = translator.translate(text)
    return translation


def text_to_speech(text, output_file):
    tts = gTTS(text=text, lang='hi')
    tts.save(output_file)


def record_and_process():
    record_seconds = int(record_duration_entry.get())
    recorded_wav = "recorded.wav"
    output_mp3 = "output.mp3"

    record_audio(recorded_wav, record_seconds)
    recognized_text = recognize_speech(recorded_wav)
    recognized_text_label.config(text=f"Recognized Text: {recognized_text}")

    translated_text = translate_to_hindi(recognized_text)
    translated_text_label.config(text=f"Translated Text: {translated_text}")

    text_to_speech(translated_text, output_mp3)
    messagebox.showinfo("Completed", f"Translation and Speech saved to {output_mp3}")


root = tk.Tk()
root.title("Speech Translator")
root.geometry("400x300")

tk.Label(root, text="Recording Duration (seconds):").pack(pady=10)
record_duration_entry = tk.Entry(root)
record_duration_entry.pack(pady=5)
record_duration_entry.insert(0, "5")

recognized_text_label = tk.Label(root, text="Recognized Text: ")
recognized_text_label.pack(pady=10)

translated_text_label = tk.Label(root, text="Translated Text: ")
translated_text_label.pack(pady=10)

process_button = tk.Button(root, text="Record and Translate", command=record_and_process)
process_button.pack(pady=20)

root.mainloop()