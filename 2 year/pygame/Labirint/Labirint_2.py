from pygame import *
import os


class Avatar(sprite.Sprite):
    def __init__(self, image_path, image_size, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (image_size, image_size))
        self.image_size = image_size
        self.x = x
        self.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.x, self.y))


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
enemy = Avatar(os.path.join(BASE_DIR, 'enemy.png'), 60, 1000, 600, 1.5)
enemy.dir = 'left'

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))
    hero.reset()
    enemy.reset()

    if keys_pressed[K_LEFT] and hero.x > 5:
        hero.x -= hero.speed
    if keys_pressed[K_RIGHT] and hero.x < window_rez_x - 5 - hero.image_size:
        hero.x += hero.speed
    if keys_pressed[K_UP] and hero.y > 5:
        hero.y -= hero.speed
    if keys_pressed[K_DOWN] and hero.y < window_rez_y - 5 - hero.image_size:
        hero.y += hero.speed

    if enemy.dir == 'left' and enemy.x > 900:
        enemy.x -= enemy.speed
    elif enemy.dir == 'left' and enemy.x <= 900:
        enemy.dir = 'right'
    if enemy.dir == 'right' and enemy.x < 1050:
        enemy.x += enemy.speed
    elif enemy.dir == 'right' and enemy.x >= 1050:
        enemy.dir = 'left'

    # if sprite.collide_rect(hero, enemy):
    #     game = False

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()