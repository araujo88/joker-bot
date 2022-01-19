import pyaudio
import wave
from noalsaerr import noalsaerr

def recordAudio(seconds):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt24  # 24 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    filename = "output.wav"

    with noalsaerr():
        p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Listening ...')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished listening.')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()