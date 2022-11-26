# The camera.

import pygame


from screen_size import SCREEN_WIDTH


pygame.init()


class CameraInit(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()

        self.camera = pygame.math.Vector2(0, 0)

        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2

        self.box_borders = {'left': 0, 'right': 200, 'top': 150, 'bottom': 100}
        self.box = pygame.Rect((0, 150), (SCREEN_WIDTH, 330))


    def camera_box(self, target):
        if target.rect.top < self.box.top:
            self.box.top = target.rect.top
        elif target.rect.bottom > self.box.bottom:
            self.box.bottom = target.rect.bottom

        self.camera.y = self.box.top - self.box_borders['top']


    def update_draw(self, dino):
        self.camera.x = dino.rect.centerx - self.half_width

        self.camera_box(dino)

        for sprite in self.sprites():
            off_camera_position = sprite.rect.topleft - self.camera
            self.display_surface.blit(sprite.image, off_camera_position)
