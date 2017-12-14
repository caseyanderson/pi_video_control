#!/usr/bin/python3

from video_player import *
import os
import signal
from gpiozero import Button

button = Button(4)

BASE_DIR = '/home/pi/'

loop_path = ''.join([BASE_DIR, 'dramatic_chipmunk.mp4'])
loop = Player(loop_path)

is_playing = False
firsttime = True

try:
    while True:
        if (button.value == False) and (is_playing == False) and (firsttime == True):
            print('tigger must be down to setup loop')
        elif (button.value == True) and (is_playing == False) and (firsttime == True):
            print('nothing is playing, start the loop')
            loop.loop()
            firsttime = False
            is_playing = True
        elif (button.value == True) and (is_playing == True) and (firsttime == False):
            print('pause')
            loop.toggle()
            is_playing = False
        elif (button.value == False) and (is_playing == False) and (firsttime == False):
            print('play')
            loop.toggle()
            is_playing = True

except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    if loop.status() is 'playing':
        print('video is playing, terminating now!')
        os.killpg(os.getpgid(play_process.pid), signal.SIGTERM)  # Send the signal to all the process groups (found this here: https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true )
    else:
        print('no video running, exiting now')
