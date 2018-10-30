#!/usr/bin/env python3

'''
wrapper for controlling omxplayer instances
'''

import subprocess
import os
import signal


class Player():

    def __init__(self, path):
        self.path = path
        self.process = None

    def loop(self):
        path = self.path
        self.process = subprocess.Popen(['omxplayer', '-b', '--no-osd', '--loop', path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def play(self):
        path = self.path
        self.process = subprocess.Popen(['omxplayer', '-b', '--no-osd', path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    def status(self):
        if self.process.poll() is not None:
            return 'done'
        else:
            return 'playing'

    def stop(self):
        self.process.stdin.write(b'q')
        self.process.stdin.flush()

    def kill(self):
        os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)

    def toggle(self):
        self.process.stdin.write(b'p')
        self.process.stdin.flush()
