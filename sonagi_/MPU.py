#import FaBo9Axis_MPU9250
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

import time
import sys
from datetime import datetime
from collections import deque

from keras.models import load_model
import numpy as np


def Pass_Data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%10000 < 1000:
                line = line + 1000

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
        
def Reset_data():
    check = 0
    while check == 0:
        try:
            f = open('recognition.txt', 'r')
            line = int(f.readline())
            # print(line)
            f.close()

            if line%10000 >= 1000:
                line = line - 1000

            f = open('recognition.txt', 'w')
            f.write(str(line))
            f.close()

            check = 1
        except:
            continue
        
def init():
    global start
    curr_time = datetime.now()
    while (datetime.now() - start).seconds < 3 :
        #try:
        curr_time = datetime.now()
        accel = mpu.readAccelerometerMaster()
        #print(accel)

        gyro = mpu.readGyroscopeMaster()
        #print(gyro)

        mag = mpu.readMagnetometerMaster()
        #print(mag)

        queue.append(sum(accel))
        
        if abs(accel[0]) > 1 and abs(accel[1]) > 1 and abs(accel[2]) > 1:
            Pass_Data()
            time.sleep(2)
            Reset_Data()

        time.sleep(0.1)
        #except:
        #    pass
        
def save_sensor_value():
    avg = sum(queue)/len(queue)
    while check == 0:
        try:
            f = open('value.txt', 'w')
            f.write(str(avg))
            f.close()

            check = 1
        except:
            continue

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # Master has 0x68 Address
    address_mpu_slave=MPU9050_ADDRESS_68, # Slave has 0x68 Address
    bus=1, 
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)
mpu.configure()

queue = deque()

print(1)


model = load_model('model.h5')
start = datetime.now()
init()
size = len(queue)

print(2)

while True:
    try:
        if (datetime.now() - start).seconds > 60:
            save_sensor_value()
            start = datetime.now()
        
        
        curr_time = datetime.now()
        accel = mpu.readAccelerometerMaster()
        print(accel)

        gyro = mpu.readGyroscopeMaster()
        print(gyro)

        mag = mpu.readMagnetometerMaster()
        print(mag)
        
        arr = accel + gyro + mag
        
        
        if model.predict_classes(np.array(arr)) == 1:
             Pass_Data()
             time.sleep(2)
             Reset_Data()
        
        #if abs(accel[0]) > 1 and abs(accel[1]) > 1 and abs(accel[2]) > 1:
        #    Pass_Data()
        #    time.sleep(2)
        #    Reset_Data()

            
        queue.popleft()
        queue.append(sum(accel))

        time.sleep(0.1)

    except KeyboardInterrupt:
        pass

