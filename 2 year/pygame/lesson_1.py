from pygame import *
from random import randint
import os

window_rez_x, window_rez_y = 1200, 800
window = display.set_mode((window_rez_x, window_rez_y))
display.set_caption("Догонялки")

clock = time.Clock()
FPS = 60

bart_size = 80
speed = 10

berry_size = 35

homer_size = 100
homer_speed = 1

background = transform.scale(image.load("picture.jpg"), (window_rez_x, window_rez_y))

bart = transform.scale(image.load('bart.png'), (bart_size, bart_size))
x1, y1 = 100, 100

berry = transform.scale(image.load('berries.jpg'), (berry_size, berry_size))
x2, y2 = randint(0, window_rez_x - berry_size + 1), randint(0, window_rez_y - berry_size + 1)

homer = transform.scale(image.load('homer.png'), (homer_size, homer_size))
x3, y3 = window_rez_x/2, window_rez_y/2

game = True
while game:
    window.blit(background, (0, 0))
    window.blit(bart, (x1, y1))
    window.blit(berry, (x2, y2))
    window.blit(homer, (x3, y3))
    clock.tick(FPS)

    keys_pressed = key.get_pressed()
    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < window_rez_x - 5 - bart_size:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < window_rez_y - 5 - bart_size:
        y1 += speed

    delta_x = x3 - x1
    if delta_x < 0:
        delta_x = -delta_x
    delta_y = y3 - y1
    if delta_y < 0:
        delta_y = -delta_y
    hipotenyza = (delta_x ** 2 + delta_y ** 2) ** 0.5
    if x3 > x1:
        x3 -= homer_speed * (delta_x / hipotenyza)
    elif x3 == x1:
        pass
    else:
        x3 += homer_speed * (delta_x / hipotenyza)
    if y3 > y1:
        y3 -= homer_speed * (delta_y / hipotenyza)
    elif y3 == y1:
        pass
    else:
        y3 += homer_speed * (delta_y / hipotenyza)

    if x1 < x2 < x1 + bart_size and y1 < y2 < y1 + bart_size\
            or x1 < x2 + berry_size < x1 + bart_size and y1 < y2 + berry_size < y1 + bart_size\
            or x1 < x2 < x1 + bart_size and y1 < y2 + berry_size < y1 + bart_size\
            or x1 < x2 + berry_size < x1 + bart_size and y1 < y2 < y1 + bart_size:
        mixer.init()
        mixer.music.load(os.path.join(os.path.curdir, 'Sound_19349.mp3'))
        mixer.music.play()
        x2 = randint(0, window_rez_x - berry_size + 1)
        y2 = randint(0, window_rez_y - berry_size + 1)

        homer_speed += 0.2
        homer_size += 10
        homer = transform.scale(image.load('homer.png'), (homer_size, homer_size))

    if x1 <= x3 <= x1 + bart_size and y1 <= y3 <= y1 + bart_size \
            or x1 <= x3 + homer_size <= x1 + bart_size and y1 <= y3 + homer_size <= y1 + bart_size\
            or x1 <= x3 + homer_size <= x1 + bart_size and y1 <= y3 <= y1 + bart_size\
            or x1 <= x3 <= x1 + bart_size and y1 <= y3 + homer_size <= y1 + bart_size:
        speed = 0
        x1 = 9999
        y1 = 9999
        homer_speed = 0
        mixer.init()
        mixer.music.load(os.path.join(os.path.curdir, 'Sound_08426.mp3'))
        mixer.music.play()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()