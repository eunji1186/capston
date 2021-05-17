import RPi.GPIO as GPIO  
import time  
  
GPIO.setmode( GPIO.BOARD )  
  

GPIO.setup(12, GPIO.OUT)  
 
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
  
  
while True:  
  
    input_state = GPIO.input(11)  
    if input_state == False:  
        GPIO.output(12, GPIO.HIGH)  
    else:  
        GPIO.output(12, GPIO.LOW)  
  
    time.sleep(0.5)  

