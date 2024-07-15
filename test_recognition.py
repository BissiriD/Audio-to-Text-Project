from vosk import Model, KaldiRecognizer
import wave
import json

model = Model(r"C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\vosk-model-en-us-0.22.zip\\vosk-model-en-us-0.22")

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

audio_file_path = "C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\playlist_1\\How “Digital Twins” Could Help Us Predict the Future Karen Willcox.wav"
transcription = transcribe_vosk(audio_file_path)
print(transcription)
    