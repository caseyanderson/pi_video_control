#!/usr/bin/python3

from video_player import *

from gpiozero import Button

button = Button(4)

BASE_DIR = '/home/pi/'

loop_path = ''.join([BASE_DIR, 'dramatic_chipmunk.mp4'])

loop = Player(loop_path)

is_playing = True
firsttime = False

loop.loop()


try:
    while True:
        if (button.value == True) and (is_playing == True) and (firsttime == False):
            print('pause')
            is_playing = False
        elif (button.value == False) and (is_playing == False) and (firsttime == False):
            print('play')
            is_playing = True

except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
