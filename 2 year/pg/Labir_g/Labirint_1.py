from pygame import *
import os

class Player(sprite.Sprite):
    def __init__(self, image_path, sprite_size, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (sprite_size, sprite_size))
        self.sprite_size = sprite_size
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3 , width, wall_x, wall_y, height):
        super().__init__()
        self.width = width
        self.height = height
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


BASE_DIR = os.path.curdir
clock = time.Clock()
FPS = 60
game = True

window_rez_x, window_rez_y = 1000, 666
window = display.set_mode((window_rez_x, window_rez_y))
display.set_caption("Лабиринт")

background = transform.scale(image.load(os.path.join(BASE_DIR, 'background.jpg')), (window_rez_x, window_rez_y))

hero = Player(os.path.join(BASE_DIR, 'hero.png'), 60, 20, 100, 5)
enemy = Player(os.path.join(BASE_DIR, 'enemy.png'), 60, 800, 500, 4)
enemy.dir = 'right'
target = Player(os.path.join(BASE_DIR, 'target.png'), 60, 850, 600, None)

for i in range(1):
    w1 = Wall(70, 130, 50, 20, 100, 0, 560)
    w2 = Wall(70, 130, 50, 20, 220, 366, 300)
    w3 = Wall(70, 130, 50, 20, 220, 100, 166)
    w4 = Wall(70, 130, 50, 150, 220, 100, 20)
    w5 = Wall(70, 130, 50, 20, 370, 0, 120)
    w6 = Wall(70, 130, 50, 270, 220, 266, 20)
    w7 = Wall(70, 130, 50, 20, 490, 100, 186)
    w8 = Wall(70, 130, 50, 20, 610, 0, 120)
    w9 = Wall(70, 130, 50, 166, 610, 100, 20)
    w10 = Wall(70, 130, 50, 20, 770, 100, 166)
    w11 = Wall(70, 130, 50, 20, 340, 366, 200)
    w12 = Wall(70, 130, 50, 450, 340, 366, 20)
    w13 = Wall(70, 130, 50, 20, 630, 466, 200)
    w14 = Wall(70, 130, 50, 160, 630, 466, 20)
    w15 = Wall(70, 130, 50, 20, 770, 366, 120)
    w16 = Wall(70, 130, 50, 20, 890, 0, 486)
    w17 = Wall(70, 130, 50, 20, 630, 233, 20)
    w18 = Wall(70, 130, 50, 20, 490, 516, 20)

mixer.init()
mixer.music.load(os.path.join(BASE_DIR, '01389.mp3'))
mixer.music.play()

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))
    hero.reset()
    enemy.reset()
    target.reset()

    for i in range(1):
        w1.reset()
        w2.reset()
        w3.reset()
        w4.reset()
        w5.reset()
        w6.reset()
        w7.reset()
        w8.reset()
        w9.reset()
        w10.reset()
        w11.reset()
        w12.reset()
        w13.reset()
        w14.reset()
        w15.reset()
        w16.reset()
        w17.reset()
        w18.reset()

    if keys_pressed[K_LEFT] and hero.rect.x > 5:
        hero.rect.x -= hero.speed
    if keys_pressed[K_RIGHT] and hero.rect.x < window_rez_x - 5 - hero.sprite_size:
        hero.rect.x += hero.speed
    if keys_pressed[K_UP] and hero.rect.y > 5:
        hero.rect.y -= hero.speed
    if keys_pressed[K_DOWN] and hero.rect.y < window_rez_y - 5 - hero.sprite_size:
        hero.rect.y += hero.speed

    if enemy.dir == 'right' and enemy.rect.x < window_rez_x - enemy.sprite_size:
        enemy.rect.x += enemy.speed
    if enemy.dir == 'right' and enemy.rect.x >= window_rez_x - enemy.sprite_size:
        enemy.dir = 'left'
    if enemy.dir == 'left' and enemy.rect.x > window_rez_x - 350:
        enemy.rect.x -= enemy.speed
    if enemy.dir == 'left' and enemy.rect.x <= window_rez_x - 350:
        enemy.dir = 'right'

    if sprite.collide_rect(hero, enemy):
        print('lose')
    if sprite.collide_rect(hero, target):
        print('win')

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()