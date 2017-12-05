# trigger a video from button press or similar input

import os
import signal
import subprocess
from gpiozero import Button

video_path = '/home/pi/dramatic_chipmunk.mp4'
input_pin = 4
is_playing = 0
play_process = None

button = Button(input_pin)

try:
    while True:
        if is_playing == 0 and button.value == True:
            print('button pressed, starting video')
            play_process = subprocess.Popen(['omxplayer', '-b', '--no-osd', video_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            preexec_fn=os.setpgrp,
            close_fds=True)
            is_playing = 1
        if is_playing == 1:
            if play_process.poll() is not None:     # the process is done when it is not None
                print(''.join(['done', '\n', '\n']))
                is_playing = 0
            # else:
            #     # print('playing')
except KeyboardInterrupt:
    print(''.join([ '\n', '\n', 'INTERRUPTED', '\n']))
    button.close()
    if play_process.poll() is None:
        print('video is running, terminating now!')
        os.killpg(os.getpgid(play_process.pid), signal.SIGTERM)  # Send the signal to all the process groups (found this here: https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true )
    else:
        print('no video running, exiting now')
