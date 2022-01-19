from record_audio import recordAudio
from transcript_audio import transcriptAudio
from computer_voice import computerVoice
from random_joke import randomJoke


computerVoice(f"Hello! I am a joker bot. Would you like to hear a joke?")

while True:
    recordAudio(3)
    transcript_audio = transcriptAudio()
    if transcript_audio is None:
        computerVoice("Sorry, I couldn't understand you. Could you say that again?")
    elif "no" in transcript_audio or "nope" in transcript_audio:
        computerVoice("That's ok. See you next time. Bye!")
        break
    elif "yes" in transcript_audio or "yeah" in transcript_audio:
        computerVoice(randomJoke())
        computerVoice("Do you want to hear another joke?")
    else:
        computerVoice("Sorry, I couldn't understand you. Could you say that again?")