#!/usr/bin/python3

from video_player import *

from gpiozero import Button

button = Button(4)

BASE_DIR = '/home/pi/'

loop_path = ''.join([BASE_DIR, 'dramatic_chipmunk.mp4'])

loop = Player(loop_path)

is_paused = False

try:
    while True:
                if (button.value == True) and (is_paused == False):
                    print('pause video')
                elif (button.value == False) and (is_paused == False):
                    print('playing video')

except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()