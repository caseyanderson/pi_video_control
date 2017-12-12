'''
wrapper for controlling omxplayer instances

currently supports init, play, loop, stop, and toggling pause

'''

import subprocess
import io

class Player():

    def __init__(self, path):     # path should be set during init
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

    def info(self):
        self.process.stdin.write(b'z')
        self.process.stdin.flush()
        line = self.process.stdout.readline()
        if line != b'':
            return line
        else:
            break

    def stop(self):         # is quit the same as terminate?
        self.process.stdin.write(b'q')
        self.process.stdin.flush()

    def toggle(self):
        self.process.stdin.write(b'p')
        self.process.stdin.flush()
