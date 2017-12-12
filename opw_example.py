#!/usr/bin/env python3

from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

VIDEO_PATH = Path("/home/pi/dramatic_chipmunk.mp4")

player = OMXPlayer(VIDEO_PATH)

sleep(1)

player.position()

sleep(2)

player.position()

sleep(3)

player.quit()

