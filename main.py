from vosk import Model, KaldiRecognizer
import os 
import wave
import json


model = Model("Path to Vosk Model")

def transcribe(audio_file_path):
    wf = wave.open(audio_file_path, "rb")
    if wf.getnchannels() != 1:
        raise ValueError("Audio file must be mono")
    
    recognizer = KaldiRecognizer(model, wf.getframerate())
    recognizer.SetWords(True)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            results.append(json.loads(recognizer.Result())['text'])

    results.append(json.loads(recognizer.FinalResult())['text'])
    return "".join(results)

def transcribe_all_files(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".wav"):
                audio_file_path = os.path.join(root, file)
                transcription = transcribe(audio_file_path)

                relative_path = os.path.relpath(audio_file_path, input_dir)
                output_file_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                with open(output_file_path.replace(".wav", ".txt"), 'w', encoding='utf-8') as f:
                    f.write(transcription)
                print(f"Transcription saved to: {output_file_path.replace('.wav', '.txt')}")


if __name__ == "__main__":
    audio_directory = "Path to Audio Directory"
    results_directory = "Path to Results Directory"
    transcribe_all_files(audio_directory, results_directory)