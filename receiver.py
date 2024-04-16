import queue
import threading
import time
import numpy as np
import pyaudio
import serial
import soundfile as sf
import socket

ser = serial.Serial("/dev/tty.usbserial-A10KQUWB", 115200)
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

p = pyaudio.PyAudio()

PLAY_CHUNK_SIZE = 128
i = 0

q = queue.Queue()
def chunk_getter():
    while True:
        t = ser.read(PLAY_CHUNK_SIZE * 4)
        t = np.frombuffer(t, np.float32)
        # print(t)
        q.put(t)

receive_thread = threading.Thread(target=chunk_getter, daemon=True)
receive_thread.start()

def get_next_chunk(in_data, frame_count, time_info, status):
    global i
    # res = data_22k[(i*PLAY_CHUNK_SIZE):((i*PLAY_CHUNK_SIZE)+PLAY_CHUNK_SIZE)]
    print(i)
    i+=1

    if q.empty():
        return np.array([0.0]*PLAY_CHUNK_SIZE, dtype=np.float32), pyaudio.paContinue
    else:
        return q.get(), pyaudio.paContinue

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=2000,
                output=True,
                frames_per_buffer=PLAY_CHUNK_SIZE,
                stream_callback=get_next_chunk)
stream.start_stream()

try:
    while True:
        time.sleep(1)
except:
    pass

stream.stop_stream()
stream.close()

p.terminate()