'''
wrapper for controlling omxplayer instances

currently supports init, play, loop, stop, and toggling pause

'''

import subprocess

class Player():
    def __init__(self,path):
        self.path = None
        self.process = None
    def play(self, path):
        self.path = path
        self.process = subprocess.Popen(['omxplayer', '-b', '--no-osd', self.path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    def loop(self, path):
        self.path = path
        self.process = subprocess.Popen(['omxplayer', '-b', '--no-osd', '--loop', self.path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    def stop(self):
        self.process.stdin.write(b'q')
        self.process.stdin.flush()
    def toggle(self):
        self.process.stdin.write(b'p')
        self.process.stdin.flush()
