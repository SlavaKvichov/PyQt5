from objects import *


while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    NER_count += 1
    NBR_count += 1

    window.blit(background, (0, 0))
    player.reset()

    if NER_count == NER:
        NER_count = 0
        enemy_generete()
    if NBR_count == NBR:
        NBR_count = 0
        bullet_generete()

    for i in enemies:
        if i.shouted == True:
            i.shouted_time += 1
            if i.shouted_time == 10:
                enemies.remove(i)
                continue
        for j in bullets:
            if sprite.collide_rect(i, j):
                bullets.remove(j)
                i.shouted = True
                i.killed()

    for i in enemies:
        i.reset()
        i.move('down')

    for i in bullets:
        i.reset()
        i.move('up')

    if keys_pressed[K_LEFT] and player.rect.x > 5:
        player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < win_rez_x - 5 - units_size:
        player.rect.x += player.speed

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()