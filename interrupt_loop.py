#!/usr/bin/env python3

'''
looping video can be interrupted by a second video,
resuming the loop from the beginning upon completion
'''

from video_player import *

from gpiozero import Button
from time import sleep

button = Button(4)

first_time = 1
interrupted = 0

BASE_DIR = '/home/pi/'

LOOP_FILENAME = 'dramatic_chipmunk.mp4'
INT_FILENAME = 'head_explode.mp4'


loop_path = ''.join([BASE_DIR, LOOP_FILENAME])
play_path = ''.join([BASE_DIR, INT_FILENAME])

v1_playing = 0
v2_playing = 0

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
