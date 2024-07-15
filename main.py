import speech_recognition as sr

def test_speech_recognition(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)

    try:
         print("Google Speech Recognition thinks you said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

audio_file_path = "C:\\Users\\Bissiri's PC\\Downloads\\speech_rec_project\\playlist_1'\\How “Digital Twins” Could Help Us Predict the Future Karen Willcox.wav"

test_speech_recognition(audio_file_path)
    