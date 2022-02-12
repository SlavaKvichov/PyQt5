from objects import *

while game:
    clock.tick(FPS)
    keys_pressed = key.get_pressed()

    window.blit(background, (0, 0))
    player.reset()

    if keys_pressed[K_LEFT] and player.rect.x > 5:
        player.rect.x -= player.speed
    if keys_pressed[K_RIGHT] and player.rect.x < win_rez_x - 5 - player.sprite_size:
        player.rect.x += player.speed

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()