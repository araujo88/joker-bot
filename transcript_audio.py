import speech_recognition as sr

def transcriptAudio():
    AUDIO_FILE = ("output.wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Sphinx
    try:
        print("Audio recognized:")
        audio_text =  r.recognize_google(audio)
        print(audio_text.lower())
        return audio_text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error; {0}".format(e))