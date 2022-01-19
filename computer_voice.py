from gtts import gTTS
from playsound import playsound

def computerVoice(text):
    print(text)
    # Language in which you want to convert
    language = 'en'
    accent = 'co.uk'

    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=text, lang=language, slow=False, tld=accent)
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("computer_voice.mp3")
    
    # Playing the converted file
    playsound("computer_voice.mp3")