#!/usr/bin/env python3

'''
trigger video playback when analog sensor crosses a value
'''

from video_player import *
import time
import Adafruit_ADS1x15

BASE_DIR = '/home/cta/'
FILENAME =  'dramatic_chipmunk.mp4'

play_path = ''.join([BASE_DIR, FILENAME])

play = Player(play_path)
adc = Adafruit_ADS1x15.ADS1015()

GAIN = 1
threshold = 500
is_playing = False

try:
    print("reading sensor values!")
    while True:
        sensor_val = adc.read_adc(0, gain=GAIN)
        if is_playing == False and sensor_val <= threshold:
            print('threshold crossed, starting video')
            play.play()
            is_playing = True
        elif is_playing == True:
            if play.status() == 'done':
                print(''.join(['done', '\n', '\n']))
                is_playing = False
except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    if play.status() == 'playing':
        print('video is running, terminating now!')
        play.kill()
    else:
        print('no video running, exiting now')
