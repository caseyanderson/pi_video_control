'''
wrapper for controlling omxplayer instances

currently supports init, play, loop, stop, and toggling pause

'''

import subprocess

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

    def stop(self):         # is quit the same as terminate?
        self.process.stdin.write(b'q')
        self.process.stdin.flush()

    def position(self):
        self.process = subprocess.Popen(['omxplayer', '-s', path], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def toggle(self):
        self.process.stdin.write(b'p')
        self.process.stdin.flush()
