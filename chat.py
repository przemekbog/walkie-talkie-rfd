import pyaudio
import numpy as np

# Parameters
CHUNK = 1024  # Number of frames per buffer
RATE = 44100  # Sampling rate

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=RATE,
                output=True,
                frames_per_buffer=CHUNK)

# Generate some example sound data (sine wave)
def generate_sine_wave(freq, duration):
    t = np.linspace(0, duration, int(RATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave.astype(np.float32)

# Main loop
while True:
    # Generate sound data
    sound_data = generate_sine_wave(440, 1.0)  # Example: 440 Hz sine wave for 1 second

    # Break sound data into chunks
    chunks = [sound_data[i:i+CHUNK] for i in range(0, len(sound_data), CHUNK)]

    # Play each chunk
    for chunk in chunks:
        stream.write(chunk)

# Stop stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
p.terminate()
