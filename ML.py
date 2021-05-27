import FaBo9Axis_MPU9250
import time
import sys

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

#df = pd.DataFrame(columns = ['ax' , 'ay' , 'az', 'gx', 'gy', 'gz', 'mx', 'my', 'mz'])
data = ''

try:
    for i in range(20):
        accel = mpu9250.readAccel()
        print(" ax = " , ( accel['x'] ))
        print( " ay = " , ( accel['y'] ))
        print( " az = " , ( accel['z'] ))
        
        gyro = mpu9250.readGyro()
        print( " gx = " , ( gyro['x'] ))
        print( " gy = " , ( gyro['y'] ))
        print( " gz = " , ( gyro['z'] ))

        mag = mpu9250.readMagnet()
        print( " mx = " , ( mag['x'] ))
        print( " my = " , ( mag['y'] ))
        print( " mz = " , ( mag['z'] ))
        
        #df = df.append({'ax':accel['x'], 'ay':accel['y'], 'az':accel['z'], 'gx':gyro['x'], 'gy':gyro['y'], 'gz':gyro['z'], 'mx':mag['x'], 'my':mag['y'], 'mz':mag['z']})
        data += str(accel['x']) +',' + str(accel['y']) + ','+ str(accel['z'])
        data += ',' + str(gyro['x'])+ ','+ str(gyro['y'])+ ','+ str(gyro['z'])
        data += ',' + str(mag['x'])+ ','+ str(mag['y'])+ ','+ str(mag['z'])
        data += '\n'
        
        

        time.sleep(0.1)
        
    f = open('data_10.txt', 'w')
    f.write(data)
    f.close()

except KeyboardInterrupt:
    sys.exit()
