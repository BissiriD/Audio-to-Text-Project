from vosk import Model, KaldiRecognizer
import wave
import json

model = Model("Path to Vosk Model")

def transcribe_vosk(audio_file_path):
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

audio_file_path = "Path to an Audio File"
transcription = transcribe_vosk(audio_file_path)

video_file = open("audio_file.txt", 'w')
video_file.write(transcription)

    