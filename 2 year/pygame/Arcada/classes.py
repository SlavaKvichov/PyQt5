from config import *

class Unit(sprite.Sprite):
    def __init__(self, image_path, x, y, size):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (size, size))
        self.sprite_size = size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))