# The pterosaur. A type of enemy.

import pygame
from random import randint

from groups import Camera, PterosaurGroup, MetalBallGroup, HeartGroup
from projectiles import MetalBall
from enemy_life_bar import LifeBar
from items import Heart


pygame.init()


class Pterosaur(pygame.sprite.Sprite):
    def __init__(self, groups, position, import_sprites):
        super().__init__(groups)

        self.direction = '(to_right)'

        self.surface = pygame.display.get_surface()

        self.image = pygame.image.load(f'Images/Enemies/Pterosaur/pterosaur0_{self.direction}.png')
        self.rect = self.image.get_rect()

        self.rect.center = position

        self.dino = import_sprites

        # ANIMATION PROPERTIES
        self.current_sprite = 0

        # HORIZONTAL MOVEMENT PROPERTIES
        self.flying_base_timer = 350
        self.flying_timer = self.flying_base_timer
        self.velocity = 6
        if self.rect.x >= 2037:
            self.direction = '(to_left)'

        # LIFE PROPERTIES
        self.life = 30
        self.life_bar = LifeBar(Camera, self)

        # METAL BALL PROPERTIES
        self.enable_metal_ball = True
        self.recharge_metal_ball = 0


    def reload_sprites(self):
        self.flying_sprites = [f'Images/Enemies/Pterosaur/pterosaur0_{self.direction}.png', f'Images/Enemies/Pterosaur/pterosaur1_{self.direction}.png']


    def animation(self):
        self.animation_list = self.flying_sprites

        self.current_sprite += 0.1

        if self.current_sprite >= len(self.animation_list):
            self.current_sprite = 0
            
        self.image = pygame.image.load(self.animation_list[int(self.current_sprite)])


    def horizontal_movement(self):
        if self.direction == '(to_right)':
            self.rect.x += self.velocity
        else:
            self.rect.x -= self.velocity

        self.flying_timer -= 1

        if self.flying_timer <= 0:
            if self.direction == '(to_right)':
                self.direction = '(to_left)'
            else:
                self.direction = '(to_right)'

            self.flying_timer = self.flying_base_timer

    
    def drop_metal_ball(self):
        close_to_dino_x = self.rect.x - self.dino.rect.x

        if -260 <= close_to_dino_x <= 348 and self.enable_metal_ball:

            if self.rect.x > self.dino.rect.x and self.direction == '(to_right)' or self.rect.x < self.dino.rect.x and self.direction == '(to_left)':
                return

            new_metal_ball = MetalBall((Camera, MetalBallGroup), self.rect.center, self.direction, self.velocity)
            self.enable_metal_ball = False

        elif not self.enable_metal_ball:
            self.recharge_metal_ball += 1

            if self.recharge_metal_ball >= 70:
                self.enable_metal_ball = True
                self.recharge_metal_ball = 0


    def dead(self):
        if self.life <= 0:
            self.life_bar.kill()
            self.kill()

            new_heart = Heart((Camera, HeartGroup), self.rect.center, self.direction, self.velocity)

            pterosaur = Pterosaur((Camera, PterosaurGroup), (randint(714, 3317), randint(0, 714)), (self.dino))


    def update(self, *args):
        self.reload_sprites()
        self.animation()
        self.horizontal_movement()
        self.drop_metal_ball()
        self.dead()
