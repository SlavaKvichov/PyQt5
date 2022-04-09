from objects import *

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    NUR_count += 1
    NBR_count += 1

    window.blit(background, (0, 0))
    window.blit(score_font, (10, 10))
    player.reset()

    for i in enemies:
        i.reset()
        i.move('down')

    for i in bullets:
        i.reset()
        i.move('up')

    if NUR_count == NUR:
        enemy_generate()
        NUR_count = 0

    for i in enemies:
        if i.shouted == True:
            if i.shouted_time == 20:
                enemies.remove(i)
            else:
                i.shouted_time += 1
        for j in bullets:
            if sprite.collide_rect(i, j):
                shouted_sound.play()
                bullets.remove(j)
                i.killed()
                i.shouted = True
                score += 1
                score_font = update_score(score)

    if keys_pressed[K_LEFT] and player.rect.x > 5:
        player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < win_rez_x - 5 - player.sprite_size:
        player.rect.x += player.speed

    if keys_pressed[K_SPACE]:
        if NBR_count > NBR:
            NBR_count = 0
            bullet_generate()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()