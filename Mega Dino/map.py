import pygame


pygame.init()


class GroundMap(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load('Images/simple_map.png')
        self.rect = self.image.get_rect()

        self.rect.topleft = (0, 0)