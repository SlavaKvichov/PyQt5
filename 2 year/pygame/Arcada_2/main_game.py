from objects import *
from random import randint

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))

    player.reset()
    if 2 > randint(1, 100):
        enemies.append(Unit(os.path.join(IMAGES_DIR, 'CID.png'),
                            randint(5, int((win_rez_x - units_size - 5))), 0, units_size, 2))
    for i in enemies:
        i.reset()

    if keys_pressed[K_LEFT] and player.rect.x > 5:
        player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < win_rez_x - 5 - units_size:
        player.rect.x += player.speed

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()