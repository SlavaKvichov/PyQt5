from pygame import *
import os


class Player(sprite.Sprite):
    def __init__(self, image_path, sprite_size, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (sprite_size, sprite_size))
        self.sprite_size = sprite_size
        self.player_x = player_x
        self.player_y = player_y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.player_x, self.player_y))


BASE_DIR = os.path.curdir
clock = time.Clock()
FPS = 60
game = True

window_rez_x, window_rez_y = 1200, 800
window = display.set_mode((window_rez_x, window_rez_y))
display.set_caption("Лабиринт")

background = transform.scale(image.load(os.path.join(BASE_DIR, 'background.jpg')), (window_rez_x, window_rez_y))

hero = Player(os.path.join(BASE_DIR, 'hero.png'), 60, 100, 100, 5)
enemy = Player(os.path.join(BASE_DIR, 'enemy.png'), 60, 1000, 600, 2)

mixer.init()
mixer.music.load(os.path.join(BASE_DIR, '01389.mp3'))
mixer.music.play()

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))
    hero.reset()
    enemy.reset()

    if keys_pressed[K_LEFT] and hero.player_x > 5:
        hero.player_x -= hero.speed
    if keys_pressed[K_RIGHT] and hero.player_x < window_rez_x - 5 - hero.sprite_size:
        hero.player_x += hero.speed
    if keys_pressed[K_UP] and hero.player_y > 5:
        hero.player_y -= hero.speed
    if keys_pressed[K_DOWN] and hero.player_y < window_rez_y - 5 - hero.sprite_size:
        hero.player_y += hero.speed

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()