from pygame import *
import os

BASE_DIR = os.path.curdir

clock = time.Clock()
FPS = 60

win_rez_x = 650
win_rez_y = win_rez_x * 1.5
units_size = win_rez_x / 7

window = display.set_mode((win_rez_x, win_rez_y))
display.set_caption("Аркада")

game = True