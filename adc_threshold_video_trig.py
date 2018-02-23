#!/usr/bin/python3
#threshold controls video playback

import sys
sys.path.insert(0, '/home/cta/pi_video_control')
import video_player

import time
import Adafruit_ADS1x15

BASE_DIR = '/home/pi/'
FILENAME =  'dramatic_chipmunk.mp4'

play_path = ''.join([BASE_DIR, FILENAME])
play = Player(play_path)
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
        play.play()
        is_playing = True
        if play.status() == 'done':
            print(''.join(['done', '\n', '\n']))
            is_playing = 0
            is_playing = False
    # Pause for half a second.
    time.sleep(0.1)
