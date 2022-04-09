from pygame import *
import os
'''Путь к файлам'''
BASE_DIR = os.path.curdir
MEDIA_DIR = os.path.join(BASE_DIR, 'Media')
'''ФПС'''
clock = time.Clock()
FPS = 60
'''Частота появления врагов'''
NUR = FPS * 1.5
NUR_count = 0
'''Частота посвления снарядов'''
NBR = FPS * 0.5
NBR_count = 0
'''Разрешения экрана и отношение обьектов к ним'''
win_rez_x = 650
win_rez_y = win_rez_x * 1.5
units_size = win_rez_x // 7
bullets_size = win_rez_x // 40
'''Создание окна и его название'''
window = display.set_mode((win_rez_x, win_rez_y))
display.set_caption("Аркада")

game = True