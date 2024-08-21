import RPi.GPIO as GPIO
import time
import datetime
import os
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
#camera.rotation = 180

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #PIR


while True:
    i = 0
    
    now = datetime.now()
    today = now.strftime("%B %d")
    current_time = now.strftime("%H;%M %p")


    if GPIO.input(23):
        print("sensor was tripped!")

        time.sleep(.5)
        
        camera.start_preview()
        camera.start_recording('/media/pi/VIDEO USB/videos/%s (%s).h264'
                               % (today, current_time))
        #camera.start_recording('/home/pi/%s (%s).h264'
                               #% (today, current_time))

        time.sleep(5)

        trip_counter = 0
        tripped = True
        
        while tripped == True:
            
            if GPIO.input(23):
                trip_counter += 1
                i = 0
                print("Sensor was tripped again! (%s)"
                    %(trip_counter))

                time.sleep(5)
                


            elif GPIO.input(23) != True:
                i += 1
                print(i)
                time.sleep(1)
                if i >= 10:
                    tripped = False
                
                
        camera.stop_recording()
        camera.stop_preview()
        print("recording stopped!") 
    
