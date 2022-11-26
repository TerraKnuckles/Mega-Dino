import pygame
from groups import Camera


pygame.init()


class RedLifeBar(pygame.sprite.Sprite):
    def __init__(self, groups, enemy, dial):
        super().__init__(groups)

        self.image = pygame.Surface((45, 4))
        self.image.fill((221, 0, 0))
        self.rect = self.image.get_rect()

        self.enemy = enemy
        self.dial = dial

    
    def update(self, *args):
        if self.enemy.life <= 0:
            self.kill()
        else:
            self.image = pygame.transform.scale(self.image, (self.enemy.life * 1.6, 4))
            self.rect.topleft = self.dial.topleft


class LifeBar(pygame.sprite.Sprite):
    def __init__(self, group, enemy):
        super().__init__(group)

        # LIFE DIAL SURFACE
        self.image = pygame.Surface((45, 4))
        self.image.fill('black')
        self.rect = self.image.get_rect()

        self.enemy = enemy

        self.red_bar = RedLifeBar(Camera, self.enemy, self.rect)


    def update(self, *args):
        self.rect.centerx = self.enemy.rect.centerx
        self.rect.bottom = self.enemy.rect.top