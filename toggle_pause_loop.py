#!/usr/bin/env python3

'''
pause looping video when trigger is released

arg1 is base directory
arg2 is media file to play
arg3 is which pin is the button

TO RUN: python3 trig_play.py /base/dir/ file.mov GPIOPIN
i.e. python3 trig_play.py /home/pi/ dramatic_chipmunk.webm 16

'''

from video_player import *
from gpiozero import Button
import os
import sys
import signal

BASE_DIR = str(sys.argv[1])
FILENAME =  str(sys.argv[2])
BUTTON_PIN = int(sys.argv[3])

button = Button(BUTTON_PIN)

loop_path = ''.join([BASE_DIR, FILENAME])
loop = Player(loop_path)

is_playing = False
first_time = True

print("ready!")

try:
    while True:
        if (button.value == False) and (is_playing == False) and (first_time == True):
            print('tigger must be down to setup loop')
        elif (button.value == True) and (is_playing == False) and (first_time == True):
            print('nothing is playing, start the loop')
            loop.loop()
            first_time = False
            is_playing = True
        elif (button.value == True) and (is_playing == True) and (first_time == False):
            print('pause')
            loop.toggle()
            is_playing = False
        elif (button.value == False) and (is_playing == False) and (first_time == False):
            print('play')
            loop.toggle()
            is_playing = True

except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    if loop.status() is 'playing':
        print('video is playing, terminating now!')
        loop.kill()
    else:
        print('no video running, exiting now')
