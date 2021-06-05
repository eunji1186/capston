import array
import pyaudio 

FORMAT = pyaudio.paInt16
CHANNELS = 1
INPUT_CHANNEL=2
RATE = 48000
CHUNK = 512

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=INPUT_CHANNEL,
                frames_per_buffer =CHUNK)

print("* recording")

while True:
    try:
        data = array.array('h')
        for i in range(0, int(RATE / CHUNK)):
            temp = data.fromstring(stream.read(CHUNK))
            print(temp)
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

print("* done recording")
