#!/usr/bin/python3
#threshold controls video playback

import sys
from video_player import *

import time
import Adafruit_ADS1x15

BASE_DIR = '/home/cta/'
FILENAME =  'dramatic_chipmunk.mp4'

play_path = ''.join([BASE_DIR, FILENAME])
adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1
threshold = 500
is_playing = False

print('Reading ADS1x15 values, press Ctrl-C to quit...')

while True:
    sensor_val = adc.read_adc(0, gain=GAIN)
    # print(''.join(['sensor val is ', str(sensor_val)]))
    if is_playing == False and sensor_val >= threshold:
        print('do nothing!')
    elif is_playing == False and sensor_val < threshold:
        print('play video')
        play = Player(play_path)
        time.sleep(0.01) # unnecessary
        play.play()
        is_playing = True
        if play.status() == 'done':
            print(''.join(['done', '\n', '\n']))
            is_playing = False
    # Pause for half a second.
    time.sleep(0.1)
