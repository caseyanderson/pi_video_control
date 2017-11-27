'''
wrapper for controlling omxplayer instances

currently supports init, play, stop, and toggling pause

'''

from player import Player()
import subprocess

class Player():
    def __init__(self):
        self.url = None
        self.process = None
    def play(self, url):
        self.url = url
        self.process = subprocess.Popen(['omxplayer', '-b', '--no-osd', self.url], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    def stop(self):
        self.process.stdin.write('q'.encode())
        # self.process.stdin.flush()        # this throws errors?
    def toggle(self):
        self.process.stdin.write(b'p')
        self.process.stdin.flush()
