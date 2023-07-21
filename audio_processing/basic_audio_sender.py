import socket
import sounddevice as sd
import numpy as np

# Set the duration of the recording in seconds.
duration = 5 # seconds

# Choose the sampling rate of the recording. 44100 is the standard for CD quality audio.
fs = 44100

# Record audio
print('Recording...')
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
print('Recording finished.')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12345)
sock.connect(server_address)

try:
    # Convert numpy array to bytes and send it
    data = myrecording.astype(np.int16).tobytes()
    sock.sendall(data)
finally:
    print('closing socket')
    sock.close()