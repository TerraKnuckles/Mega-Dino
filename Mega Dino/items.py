import pygame


pygame.init()


class Heart(pygame.sprite.Sprite):
    def __init__(self, groups, position, direction, acceleration):
        super().__init__(groups)

        self.image = pygame.image.load('Images/Items/heart.png')
        self.rect = self.image.get_rect()

        self.rect.center = position

        # CURE PROPERTIES
        self.cure = 5

        # GRAVITY PROPERTIES
        self.gravity_enabled = True
        self.gravity_force_limit = 6
        self.gravity_force = 0
        self.lock_gravity_force = False

        # HORIZONTAL MOVEMENT PROPERTIES
        self.acceleration = acceleration
        self.direction = direction
    

    def gravity(self):
        if self.gravity_enabled:
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


    def update(self, *args):
        self.gravity()
        self.horizontal_movement()
