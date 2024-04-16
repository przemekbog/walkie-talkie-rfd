import audioop
import time
import librosa
import serial
import soundfile as sf

ser = serial.Serial("/dev/tty.usbserial-A10KQMP1", 115200)

filename = librosa.ex('trumpet')
data, samplerate = sf.read(filename, dtype='float32')
data = data.T
data_22k = librosa.resample(data, orig_sr=samplerate, target_sr=2000)

print(len(data_22k))

PLAY_CHUNK_SIZE = 128
for i in range(len(data_22k) // PLAY_CHUNK_SIZE):
    t = data_22k[i*PLAY_CHUNK_SIZE:i*PLAY_CHUNK_SIZE+PLAY_CHUNK_SIZE]
    print(t)
    ser.write(data_22k[i*PLAY_CHUNK_SIZE:i*PLAY_CHUNK_SIZE+PLAY_CHUNK_SIZE])
    print(i)




# for i in range(50):
#     ser.write(bytearray([12])*100)
#     time.sleep(0.01)
