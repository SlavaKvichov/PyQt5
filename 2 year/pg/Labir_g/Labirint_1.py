from pygame import *
# from time import *
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

o = 0

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
for i in range(1):
    target1 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 270, 20, None)
    target2 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 270, 150, None)
    target3 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 670, 20, None)
    target4 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 920, 20, None)
    target5 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 670, 150, None)
    target6 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 400, 410, None)
    target7 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 670, 400, None)
    target8 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 680, 570, None)
    target9 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 790, 570, None)
    target10 = Player(os.path.join(BASE_DIR, 'target.png'), 60, 920, 570, None)
for i in range(1):
    w1 = Wall(70, 130, 50, 20, 100, 0, 560)
    w2 = Wall(70, 130, 50, 20, 220, 366, 300)
    w3 = Wall(70, 130, 50, 20, 220, 100, 146)
    w4 = Wall(70, 130, 50, 150, 220, 100, 20)
    w5 = Wall(70, 130, 50, 20, 370, 0, 120)
    w6 = Wall(70, 130, 50, 270, 220, 246, 20)
    w7 = Wall(70, 130, 50, 20, 490, 100, 166)
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

# mixer.init()
# mixer.music.load(os.path.join(BASE_DIR, '01389.mp3'))
# mixer.music.play()

vision_win = False
vision_lose = False

init()
f1 = font.SysFont('Arial', 24)
f2 = font.SysFont('Arial', 120)
text1 = f1.render('Ваш беляшный счёт:', True, (200, 200, 200))
text3 = f2.render('YOU LOSE!', True, (200, 0, 0))
text4 = f2.render('YOU WIN!', True, (0, 0, 200))

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))
    hero.reset()
    enemy.reset()

    text2 = f1.render(str(o), True, (200, 200, 200))

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

    for i in range(1):
        target1.reset()
        target2.reset()
        target3.reset()
        target4.reset()
        target5.reset()
        target6.reset()
        target7.reset()
        target8.reset()
        target9.reset()
        target10.reset()

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

    if sprite.collide_rect(hero, enemy) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or \
        sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5) or \
        sprite.collide_rect(hero, w6) or sprite.collide_rect(hero, w7) or sprite.collide_rect(hero, w8) or \
        sprite.collide_rect(hero, w9) or sprite.collide_rect(hero, w10) or sprite.collide_rect(hero, w11) or \
        sprite.collide_rect(hero, w12) or sprite.collide_rect(hero, w13) or sprite.collide_rect(hero, w14) or \
        sprite.collide_rect(hero, w15) or sprite.collide_rect(hero, w16) or sprite.collide_rect(hero, w17):
        # print('lose')
        hero.speed = 0
        enemy.speed = 0
        if vision_lose == True:
            time.wait(5000)
            game = False
        vision_lose = True

    if sprite.collide_rect(hero, target1):
        print('win')
        target1.rect.x = 3000
        target1.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target2):
        print('win')
        target2.rect.x = 3000
        target2.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target3):
        print('win')
        target3.rect.x = 3000
        target3.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target4):
        print('win')
        target4.rect.x = 3000
        target4.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target5):
        print('win')
        target5.rect.x = 3000
        target5.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target6):
        print('win')
        target6.rect.x = 3000
        target6.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target7):
        print('win')
        target7.rect.x = 3000
        target7.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target8):
        print('win')
        target8.rect.x = 3000
        target8.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target9):
        print('win')
        target9.rect.x = 3000
        target9.rect.y = 3000
        o += 1
    if sprite.collide_rect(hero, target10):
        print('win')
        target10.rect.x = 3000
        target10.rect.y = 3000
        o += 1

    if o == 10:
        hero.speed = 0
        enemy.speed = 0
        if vision_win == True:
            time.wait(5000)
            game = False
        vision_win = True


    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(text1, (0, 0))
    window.blit(text2, (235, 0))
    if vision_lose == True:
        window.blit(text3, (200, 250))
    if vision_win == True:
        window.blit(text4, (210, 250))

    display.update()