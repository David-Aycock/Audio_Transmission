import socket
import numpy as np
from scipy.io.wavfile import write

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
sock.bind(server_address)
print('starting up on {} port {}'.format(*server_address))

# Listen for incoming connections
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from ', client_address)

        # Receive the data in small chunks and reassemble it
        data = b''
        while True:
            chunk = connection.recv(16)
            if chunk:
                # Concatenate all chunks to get the full data
                data += chunk
            else:
                # No more data, exits the loop
                break
        # Convert bytes to numpy array and save as .wav file
        audio_data = np.frombuffer(data, dtype=np.int16)
        write('C:/Users/Aycoc/OneDrive/Desktop/Audio_Python/output.wav', 44100, audio_data)
    
    finally:
        # Clean up the connection
        connection.close()