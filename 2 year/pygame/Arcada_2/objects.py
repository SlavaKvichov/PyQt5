from classes import *
from random import randint
import os
'''Фон'''
background = transform.scale(image.load(os.path.join(IMAGES_DIR, 'background.jpg')), (win_rez_x, win_rez_y))
'''Игрок'''
player = Unit(os.path.join(IMAGES_DIR, 'x-wing.png'), win_rez_x / 2 - units_size / 2, win_rez_y * 7 / 8, units_size, 10)
'''Враги'''
def enemy_generete():
    enemies.append(Unit(os.path.join(IMAGES_DIR, 'CID.png'),
                        randint(5, win_rez_x - units_size - 5), 0, units_size, 2))
enemies = []
'''Снаряды'''
def bullet_generete():
    bullets.append(Unit(os.path.join(IMAGES_DIR, 'Bullet.png'),
                        player.rect.x + units_size / 2 - bullets_size / 2, player.rect.y, bullets_size, 15))
bullets = []
'''Фонт'''
'''Музыка'''