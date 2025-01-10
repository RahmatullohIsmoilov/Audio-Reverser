import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write as write_wav

def record_audio(duration):
    # Record audio for the given duration
    fs = 44100  # Sample rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return recording.flatten()

def save_reversed_audio(data, filename):
    # Reverse the audio and save it to a new file
    reversed_data = np.flip(data)
    fs = 44100  # Sample rate
    write_wav(filename, fs, reversed_data.astype(np.float32))

def main():
    duration = 5  # Specify the duration of the recording in seconds
    filename = "reversed_audio.wav"  # Name of the file to be saved

    print("Recording audio...")
    recorded_data = record_audio(duration)

    print("Saving reversed audio...")
    save_reversed_audio(recorded_data, filename)
    
    print(f"Reversed audio saved as {filename}")

main()
