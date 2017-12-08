#!/usr/bin/python3

from video_player import *

from gpiozero import Button
from time import sleep

button = Button(4)

first_time = 1
interrupted = 0

BASE_DIR = '/home/pi/'

loop = Player(''.join([BASE_DIR, 'dramatic_chipmunk.mp4']))
play = Player(''.join([BASE_DIR, 'head_explode.mp4']))

try:
    while True:
        if (button.value == False) and (first_time == 1):
            print('starting loop')
            loop.loop()
            first_time = 0

        elif (button.value == True) and (first_time == 0):
            print('interrupt')
            loop.toggle()
            play.play()
            interrupted = 1

        elif (first_time == 0) and (interrupted == 1):
            if play.status() == 'done':
                print('going back to loop')
                loop.toggle()
                interrupted = 0

except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()

