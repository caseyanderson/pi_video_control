#!/usr/bin/env python3

'''
pause looping video when trigger is released
'''

from video_player import *
import os
import signal
from gpiozero import Button

button = Button(4)

BASE_DIR = '/home/pi/'
FILENAME = 'dramatic_chipmunk.mp4'

loop_path = ''.join([BASE_DIR, FILENAME])
loop = Player(loop_path)

is_playing = False
first_time = True

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
