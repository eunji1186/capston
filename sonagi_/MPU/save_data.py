#import FaBo9Axis_MPU9250
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import time
import sys
import pandas as pd

#mpu9250 = FaBo9Axis_MPU9250.MPU9250()

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

df = pd.DataFrame(columns = ['ax' , 'ay' , 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz'])

try:
    for i in range(1000):
        print(i)
        accel = mpu.readAccelerometerMaster()
        #print(" ax = " , ( accel['x'] ))
        #print( " ay = " , ( accel['y'] ))
        #print( " az = " , ( accel['z'] ))
        
        gyro = mpu.readGyroscopeMaster()
        #print( " gx = " , ( gyro['x'] ))
        #print( " gy = " , ( gyro['y'] ))
        #print( " gz = " , ( gyro['z'] ))

        mag = mpu.readMagnetometerMaster()
        #print( " mx = " , ( mag['x'] ))
        #print( " my = " , ( mag['y'] ))
        #print( " mz = " , ( mag['z'] ))
        
        df = df.append({'ax':accel[0], 'ay':accel[1], 'az':accel[2], 'gx':gyro[0], 'gy':gyro[1], 'gz':gyro[2], 'mx':mag[0], 'my':mag[1], 'mz':mag[2]}, ignore_index=True)
        #print(df)
        
        time.sleep(0.1)
        
    df.to_csv("0605-stop.csv")

except KeyboardInterrupt:
    sys.exit()

