import pygame
import sys

from robot_hat import Music

m = Music()

song = sys.argv[1]

m.sound_play(song)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
