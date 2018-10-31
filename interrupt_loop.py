#!/usr/bin/env python3

'''
looping video can be interrupted by a second video,
resuming the loop from the beginning upon completion

arg1 is base directory
arg2 is loop file to play
arg3 is interruption file to play
arg4 is which pin is the button
arg5 is which pin is the LED

TO RUN: python3 interrupt_loop.py /base/dir/ loopfile.mov intteruptfile.mov BUTTON_PIN LED_PIN
i.e. python3 interrupt_loop.py /home/pi/ dramatic_chipmunk.webm head_explode.webm 16 17

'''

from video_player import *
from gpiozero import Button
from gpiozero import LED
from time import sleep
import sys

BASE_DIR = str(sys.argv[1])
LOOP_FILENAME =  str(sys.argv[2])
INT_FILENAME =  str(sys.argv[3])
BUTTON_PIN = int(sys.argv[4])
LED_PIN = int(sys.argv[5])

button = Button(BUTTON_PIN)
led = LED(LED_PIN)

first_time = 1
interrupted = 0

loop_path = ''.join([BASE_DIR, LOOP_FILENAME])
play_path = ''.join([BASE_DIR, INT_FILENAME])

v1_playing = 0
v2_playing = 0

#print("ready!")
led.on()

try:
    while True:
        if (v1_playing == 0) and (v2_playing == 0) and (button.value == False):
            print(''.join(['no videos playing, starting v1', '\n', '\n']))
            loop = Player(loop_path)
            loop.play()
            v1_playing = 1

        elif (v1_playing == 1) and (v2_playing == 0) and (button.value == False):
            if loop.status() == 'done':
                print('v1 is done')
                v1_playing = 0

        elif (v1_playing == 1) and (button.value == True):

            print('v1 interrupted!')
            loop.stop()
            play = Player(play_path)
            play.play()
            v1_playing = 0
            v2_playing = 1

        elif (v1_playing == 0) and (v2_playing == 1) and (button.value == False):
            if play.status() == 'done':
                print('v2 is done')
                v2_playing = 0

except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    led.close()
