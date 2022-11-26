import pygame


pygame.init()


class WaterBox(pygame.sprite.Sprite):
    def __init__(self, groups, position, size):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()

        self.rect.topleft = position
