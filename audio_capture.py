import os
import json
import pyaudio
import wave
from vosk import Model, KaldiRecognizer

model_path = "Path to Vosk Model"
model = Model(model_path)

def transcribe_from_mic():
    recognizer = KaldiRecognizer(model, 16000)
    recognizer.SetWords(True)

    # Initialize PyAudio
    p = pyaudio.PyAudio()

    
    # Open Stream
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=8000)
    stream.start_stream()

    print("Listening...")

    results = []

    try:
        while True:
            data = stream.read(4000)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print(result['text'])
                results.append(result['text'])
            else:
                partial_result = json.loads(recognizer.PartialResult())
                print(partial_result['partial'])
    except KeyboardInterrupt:
        print("Stopped listening.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

    
    # Join results and save to a file
    transcription = ''.join(results)
    with open('mic_transcription.txt', 'w', encoding='utf-8') as f:
        f.write(transcription)
    print("Transcription saved to mic_transcription.txt")

if __name__ == "__main__":
    transcribe_from_mic()