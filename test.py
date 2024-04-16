
import soundfile as sf
import librosa
import pyaudio
import time

# Get example audio file
filename = librosa.ex('trumpet')

data, samplerate = sf.read(filename, dtype='float32')
data = data.T
data_22k = librosa.resample(data, orig_sr=samplerate, target_sr=2000)

print(len(data_22k))
p = pyaudio.PyAudio()

PLAY_CHUNK_SIZE = 128
i = 0
def get_next_chunk(in_data, frame_count, time_info, status):
    global i
    res = data_22k[(i*PLAY_CHUNK_SIZE):((i*PLAY_CHUNK_SIZE)+PLAY_CHUNK_SIZE)]
    i+=1
    

    return res, pyaudio.paContinue

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