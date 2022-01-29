from pygame import *
import os


class Avatar(sprite.Sprite):
    def __init__(self, image_path, image_size, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (image_size, image_size))
        self.image_size = image_size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, x, y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


clock = time.Clock()
FPS = 60
game = True
BASE_DIR = os.path.curdir

mixer.init()
mixer.music.load(os.path.join(BASE_DIR, '01389.mp3'))
mixer.music.play()

window_rez_x, window_rez_y = 1200, 800
window = display.set_mode((window_rez_x, window_rez_y))
display.set_caption("Лабиринт")

background = transform.scale(image.load(os.path.join(BASE_DIR, 'background.jpg')), (window_rez_x, window_rez_y))

hero = Avatar(os.path.join(BASE_DIR, 'hero.png'), 60, 100, 100, 4)
enemy = Avatar(os.path.join(BASE_DIR, 'enemy.png'), 60, 1000, 600, 2)
enemy.dir = 'left'
target = Avatar(os.path.join(BASE_DIR, 'target.png'), 60, 950, 710, None)

w1 = Wall(232, 191, 27, 300, 40, 30, 550)
w2 = Wall(232, 191, 27, 300, 40, 700, 30)
w3 = Wall(232, 191, 27, 450, 210, 30, 550)
w4 = Wall(232, 191, 27, 600, 40, 30, 550)
w5 = Wall(232, 191, 27, 600, 580, 110, 30)
w6 = Wall(232, 191, 27, 750, 170, 250, 300)
w7 = Wall(232, 191, 27, 830, 470, 50, 290)

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))
    hero.reset()
    enemy.reset()
    target.reset()

    w1.reset()
    w2.reset()
    w3.reset()
    w4.reset()
    w5.reset()
    w6.reset()
    w7.reset()

    if keys_pressed[K_LEFT] and hero.rect.x > 5:
        hero.rect.x -= hero.speed
    if keys_pressed[K_RIGHT] and hero.rect.x < window_rez_x - 5 - hero.image_size:
        hero.rect.x += hero.speed
    if keys_pressed[K_UP] and hero.rect.y > 5:
        hero.rect.y -= hero.speed
    if keys_pressed[K_DOWN] and hero.rect.y < window_rez_y - 5 - hero.image_size:
        hero.rect.y += hero.speed

    if enemy.dir == 'left' and enemy.rect.x > window_rez_x - 300:
        enemy.rect.x -= enemy.speed
    elif enemy.dir == 'left' and enemy.rect.x <= window_rez_x - 300:
        enemy.dir = 'right'
    if enemy.dir == 'right' and enemy.rect.x < window_rez_x - 50 - enemy.image_size:
        enemy.rect.x += enemy.speed
    elif enemy.dir == 'right' and enemy.rect.x >= window_rez_x - 50 - enemy.image_size:
        enemy.dir = 'left'

    if sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, enemy) or \
        sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or \
        sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or \
        sprite.collide_rect(hero, w6) or sprite.collide_rect(hero, w7):
        game = False
    if sprite.collide_rect(hero, target):
        game = False

    # import time
    #
    # timing = time.time()
    # while True:
    #     if time.time() - timing > 10.0:
    #         timing = time.time()
    #         print("10 seconds")

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()