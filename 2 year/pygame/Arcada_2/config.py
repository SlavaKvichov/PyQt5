from pygame import *
import os
'''Путь к файлам'''
BASE_DIR = os.path.curdir
IMAGES_DIR = os.path.join(BASE_DIR, 'Images')
'''ФПС'''
clock = time.Clock()
FPS = 60
'''Разрешение экрана и других обьектов'''
win_rez_x = 650
win_rez_y = win_rez_x * 1.5
units_size = win_rez_x // 7
bullets_size = win_rez_x // 40
'''Счётчик и частота появления обьектов'''
NER = FPS * 1.5
NER_count = 0
NBR = FPS * 0.5
NBR_count = 0
'''Создание окна и его названия'''
window = display.set_mode((win_rez_x, win_rez_y))
display.set_caption("Аркада")

game = True