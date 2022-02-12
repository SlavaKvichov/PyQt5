from pygame import *
import os

BASE_DIR = os.path.curdir
IMAGES_DIR = os.path.join(BASE_DIR, 'Images')

clock = time.Clock()
FPS = 60

win_rez_x = 650
win_rez_y = win_rez_x * 1.5

units_size = win_rez_x / 7

game = True

window = display.set_mode((win_rez_x, win_rez_y))
display.set_caption("Аркада")