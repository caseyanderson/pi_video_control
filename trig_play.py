#!/usr/bin/env python3

'''
trigger a video from button press or similar

arg1 is base directory
arg2 is media file to play
arg3 is which pin is the button

TO RUN: python3 trig_play.py /base/dir/ file.mov GPIOPIN
i.e. python3 trig_play.py /home/pi/ dramatic_chipmunk.webm 16

'''

from video_player import *
from gpiozero import Button
import sys

BASE_DIR = str(sys.argv[1])
FILENAME =  str(sys.argv[2])
BUTTON_PIN = int(sys.argv[3])

play_path = ''.join([BASE_DIR, FILENAME])

is_playing = 0

button = Button(BUTTON_PIN)
play = Player(play_path)

try:
    while True:
        if is_playing == 0 and button.value == True:
            print('button pressed, starting video')
            play.play()
            is_playing = 1
        elif is_playing == 1:
            if play.status() == 'done':
                print(''.join(['done', '\n', '\n']))
                is_playing = 0
except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    if play.status() == 'playing':
        print('video is running, terminating now!')
        play.kill()
    else:
        print('no video running, exiting now')
