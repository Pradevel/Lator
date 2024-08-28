import pyaudio
import wave
import json
from vosk import Model, KaldiRecognizer
from gtts import gTTS
from deep_translator import GoogleTranslator

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


if __name__ == "__main__":
    recorded_wav = "recorded.wav"
    output_mp3 = "output.mp3"
    record_audio(recorded_wav)
    recognized_text = recognize_speech(recorded_wav)
    print("Recognized Text:", recognized_text)

    translated_text = translate_to_hindi(recognized_text)
    print("Translated Text:", translated_text)

    text_to_speech(translated_text, output_mp3)
    print(f"Translation and Speech saved to {output_mp3}")