import pygame


pygame.init()


class ChargingShotAnimation(pygame.sprite.Sprite):
    def __init__(self, groups, object):
        super().__init__(groups)

        self.charging_shot_sprites = ['Images/Effects/Dino_Charging_Shot/charging0.png','Images/Effects/Dino_Charging_Shot/charging1.png', 'Images/Effects/Dino_Charging_Shot/charging2.png', 'Images/Effects/Dino_Charging_Shot/charging3.png', 'Images/Effects/Dino_Charging_Shot/charging4.png', 'Images/Effects/Dino_Charging_Shot/charging5.png']
        self.charging_done_sprites = ['Images/Effects/Dino_Charging_Shot/charging_done0.png','Images/Effects/Dino_Charging_Shot/charging_done1.png']

        self.image = pygame.image.load(self.charging_shot_sprites[0])
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()

        self.object = object

        self.current_charging_sprite = 0


    def update(self, *args):
        if self.object.charging_shot >= 30:
            if self.object.charging_shot >= 85:
                animation_list = self.charging_done_sprites
                self.rect.bottomright = (self.object.rect.right + 12, self.object.rect.bottom + 7)
            else:
                animation_list = self.charging_shot_sprites
                self.rect.center = self.object.rect.center

            self.current_charging_sprite += 0.2

            if self.current_charging_sprite >= len(animation_list):
                self.current_charging_sprite = 0

            self.image = pygame.image.load(animation_list[int(self.current_charging_sprite)])
            self.image.set_alpha(255)

        else:
            self.image.set_alpha(0)
            self.current_charging_sprite = 0
