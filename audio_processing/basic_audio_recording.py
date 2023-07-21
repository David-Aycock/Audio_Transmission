import sounddevice as sd
from scipy.io.wavfile import write

# Sets the duration of the recording in seconds.
duration = 5 # seconds

#Choose the sample rate of the recording. 44100 is the standard for CD quality audio.
fs = 44100

#Record audio
print("Recording...")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
print("Recording finished.")

# Save as a .wav file
write('C:/Users/Aycoc/OneDrive/Desktop/Audio_Python/output.wav', fs, myrecording)