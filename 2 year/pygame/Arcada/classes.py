from config import *

class Unit(sprite.Sprite):
    def __init__(self, image_path, x, y, size, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (size, size))
        self.sprite_size = size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.shouted = False
        self.shouted_time = 0

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, side):
        if side == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def killed(self):
        self.image = transform.scale(image.load(os.path.join(MEDIA_DIR, 'Shot.png')), (self.sprite_size, self.sprite_size))