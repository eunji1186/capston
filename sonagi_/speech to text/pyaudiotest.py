import pyaudio
import time
import numpy as np
 
CHUNK = 212
RATE = 44100

#model = Model("Model")
#rec = KaldiRecognizer(model, 16000)


def init():
    global p, stream
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK,input_device_index=2)

def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%1000 < 100:
                line = line + 100

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
        
p = None
stream = None
init()

i = 0
while(True):
    try:
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        if np.average(np.abs(data)) > 4000:
            print(1)
            Pass_Data()
            time.sleep(1)
    except:
        init()
    #print(int(np.average(np.abs(data))))
    #i += 1
    #if i > 20:
    #    break

stream.stop_stream()
stream.close()
p.terminate()
