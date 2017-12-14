#!/usr/bin/python3

'''
trigger a video from button press or similar
'''

from video_player import *
from gpiozero import Button

BASE_DIR = '/home/pi/'
FILENAME =  'dramatic_chipmunk.mp4'

play_path = ''.join([BASE_DIR, FILENAME])

input_pin = 4
is_playing = 0

button = Button(input_pin)
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
