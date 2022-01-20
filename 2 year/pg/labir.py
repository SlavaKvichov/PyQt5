from pygame import *
from random import *
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
background = transform.scale(image.load("dark-4487690_960_720.jpg"),(700, 500))
game = True
o = 0
sprite1 = transform.scale(image.load('ТРЕУГОЛЬНЫЙ БЕЛЯШ.png'), (100, 100))
sprite2 = transform.scale(image.load('КРУГЛЫЙ БЕЛЯШ.png'), (65, 65))
x1, y1 = 100, 100
x2, y2 = 200, 400
clock = time.Clock()
FPS = 60
speed = 10
init()
f1 = font.SysFont('Arial', 24)
text2 = f1.render('Ваш беляшный счёт:', True, (180, 0, 0))
while game:
    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed

    text1 = f1.render(str(o), True, (180, 0, 0))

    if x1 < x2 < x1 + 65 and y1 < y2 < y1 + 65:
    # if x2 < x1 +100 and y2 < y1+100:
        x2 = randint(10, 626)
        y2 = randint(10, 426)
        o += 1
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))
    window.blit(text2, (0, 0))
    window.blit(text1, (235, 0))
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()