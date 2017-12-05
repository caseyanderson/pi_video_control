#!/usr/bin/python3
# trig camera recording via GPIO signal for certain duration

from gpiozero import Button
from gpiozero import LED
from picamera import PiCamera
from datetime import datetime
from time import sleep

# setup led and button
button = Button(4)
led = LED(17)

# recording flag
is_recording = 0

# duration to record
duration = 5

try:
    while True:

        if (button.value == True) and (is_recording == 0):
            print('setting up camera')
            camera = PiCamera()
            sleep(2)
            print("RECORDING")
            camera.start_preview()
            x = datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
            path = ''.join(['/home/pi/', x, '.h264'])
            camera.start_recording(path)
            is_recording = 1
            led.on()
            sleep(duration)
            print("DONE RECORDING!")
            camera.stop_recording()
            camera.stop_preview()
            led.off()
            camera.close()
            is_recording = 0

except KeyboardInterrupt:
    print("INTERRUPTED!")
    button.close()
    camera.close()
    led.close()
