#!/usr/bin/env python3

import socket
import wave
import pyaudio

IP = '127.0.0.1'
PORT = 6789

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "output.wav"

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((IP, PORT))
soc.listen()

frames = []
conn, addr = soc.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        frames.append(data)
        if not data:
            break

a = input()

p = pyaudio.PyAudio()
# write to file
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
