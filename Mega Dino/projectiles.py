# The projectiles of all characters that shot something.

import pygame

pygame.init()


class DinoShot(pygame.sprite.Sprite):
    def __init__(self, groups, position, direction, blast_type):
        super().__init__(groups)

        self.image = pygame.image.load(f'Images/Projectiles/Meteors/{blast_type}_meteor_{direction}.png')
        self.rect = self.image.get_rect()

        self.rect.center = position
        self.direction = direction

        if blast_type == 'small':
            self.damage = 2
        else:
            self.damage = 30

        self.pixels_traveled = 0


    def update(self, *args):
        if self.direction == '(to_right)':
            self.rect.x += 20
        else:
            self.rect.x -= 20

        self.pixels_traveled += 20

        if self.pixels_traveled >= 1400:
            self.kill()


class MetalBall(pygame.sprite.Sprite):
    def __init__(self, groups, position, direction, acceleration):
        super().__init__(groups)

        self.image = pygame.image.load('Images/Projectiles/metal_ball.png')
        self.rect = self.image.get_rect()

        self.start_position_x = self.rect.x
        self.start_position_y = self.rect.y

        self.rect.center = position
        self.direction = direction

        self.damage = 30

        # GRAVITY PROPERTIES
        self.gravity_force_limit = 6
        self.gravity_force = 0
        self.lock_gravity_force = False

        # HORIZONTAL MOVEMENT PROPERTIES
        self.acceleration = acceleration

        # ROTATION PROPERTIES
        self.rotation_timer = 0

    
    def gravity(self):
        if self.gravity_force >= self.gravity_force_limit:
            self.lock_gravity_force = True

        if not self.lock_gravity_force:
            self.gravity_force += 0.2

        self.rect.y += self.gravity_force


    def horizontal_movement(self):
        if self.direction == '(to_right)':
            self.rect.x += self.acceleration
        else:
            self.rect.x -= self.acceleration

        if not self.acceleration <= 0.3:
            self.acceleration -= 0.06
        else:
            self.acceleration = 0


    def rotation(self):
        if self.rotation_timer >= 5:
            rotation_angle = -90 if self.direction == '(to_right)' else 90
            self.image = pygame.transform.rotate(self.image, rotation_angle)
            self.rotation_timer = 0

        self.rotation_timer += 1


    def update(self, *args):
        self.gravity()
        self.horizontal_movement()
        self.rotation()
