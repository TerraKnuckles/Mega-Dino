# Basically, the dino is the player, of course.

import pygame
from keyboard import is_pressed

from projectiles import DinoShot
from groups import DinoShotGroup, Camera
from charging_shot_animation import ChargingShotAnimation


pygame.init()


class Dino(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.sprites_direction = '(to_right)'

        self.image = pygame.image.load(f'Images/Dino_{self.sprites_direction}/dino_standing.png')
        self.rect = self.image.get_rect()

        self.on_the_floor = False

        # START POSITION
        self.rect.topleft = (1528, 719)

        # MOVEMENT PROPERTIES
        self.can_move_left = True
        self.can_move_right = True
        self.current_walk_sprite = 0

        # JUMP PROPERTIES
        self.jump_force = 16
        self.enable_jump = True
        self.used_jump = False

        # GRAVITY PROPERTIES
        self.stop_gravity = False
        self.gravity_force_limit = 9
        self.gravity_force = self.gravity_force_limit
        self.lock_gravity_force = False

        # CROUCHING PROPERTIES
        self.is_crouching = False

        # SHOT PROPERTIES
        self.shot_y_position = self.rect.centery
        self.enable_shot = True
        self.charging_shot = 0
        self.charged_shot_enabled = False
        self.current_charging_sprite = 0
        self.charging_shot_animation = ChargingShotAnimation(Camera, self)

        # BLINK PROPERTIES
        self.blink_timer = 80
        self.current_blink_sprite = 0

        # LIFE PROPERTIES
        self.life = 100
        self.life_timer = 80
        self.damage = False
        self.life_dial = pygame.image.load('Images/GUI/life_bar.png')
        self.life_bar = pygame.Rect((63, 24), (182, 28))
        self.current_damaged_sprite = 0
        self.enable_dino_actions = True


    def reload_sprites(self):
        self.standing_sprite = f'Images/Dino_{self.sprites_direction}/dino_standing.png'
        self.standing_blink_sprite = f'Images/Dino_{self.sprites_direction}/dino_standing_blink.png'
        self.crouch_stopped_sprite = f'Images/Dino_{self.sprites_direction}/dino_crouching_stop.png'
        self.crouch_stopped_blink_sprite = f'Images/Dino_{self.sprites_direction}/dino_crouching_stop_blink.png'
        self.die_sprite = f'Images/Dino_{self.sprites_direction}/dino_die.png'
        self.walking_sprites = [f'Images/Dino_{self.sprites_direction}/dino_walking0.png', f'Images/Dino_{self.sprites_direction}/dino_walking1.png']
        self.walking_crouch_sprites = [f'Images/Dino_{self.sprites_direction}/dino_crouching0.png', f'Images/Dino_{self.sprites_direction}/dino_crouching1.png']
        self.took_damage_sprites = [f'Images/Dino_{(self.sprites_direction)}/dino_standing_damaged.png', f'Images/Dino_{self.sprites_direction}/dino_die.png']


    def walk(self, key):
        if key[pygame.K_LEFT] and self.can_move_left:
            self.sprites_direction = '(to_left)'
            self.rect.x -= 5

        if key[pygame.K_RIGHT] and self.can_move_right:
            self.sprites_direction = '(to_right)'
            self.rect.x += 5


    def jump(self, key):
        if key[pygame.K_UP] and self.enable_jump and not self.is_crouching:
            self.stop_gravity = True

            self.rect.y -= self.jump_force
            self.jump_force -= 0.7

            if self.jump_force <= 0:
                self.enable_jump = False
        
        elif not key[pygame.K_UP] and self.jump_force > 0:
            self.enable_jump = False
            self.jump_force = 0


    def crouch(self, key):
        if key[pygame.K_DOWN]:
            self.is_crouching = True
            self.image = pygame.image.load(self.crouch_stopped_sprite)
            self.shot_y_position = self.rect.centery + 15
        else:
            self.is_crouching = False
            self.image = pygame.image.load(self.standing_sprite)
            self.shot_y_position = self.rect.centery


    def walking_animation(self, key):
        if not self.on_the_floor:
            return

        if is_pressed('left arrow+right arrow'):
            return

        if key[pygame.K_LEFT] or key[pygame.K_RIGHT]:
            animation_list = self.walking_sprites

            if key[pygame.K_DOWN]:
                animation_list = self.walking_crouch_sprites

            self.current_walk_sprite += 0.2

            if self.current_walk_sprite >= len(animation_list):
                self.current_walk_sprite = 0
                
            self.image = pygame.image.load(animation_list[int(self.current_walk_sprite)])


    def shot(self, key):
        if key[pygame.K_x]:
            self.charging_shot += 1

            if self.enable_shot:
                new_shot = DinoShot((Camera, DinoShotGroup), (self.rect.centerx, self.shot_y_position), self.sprites_direction, 'small')
                self.enable_shot = False

            elif self.charging_shot >= 85:
                self.charged_shot_enabled = True
                self.charging_shot = 85

        else:
            self.enable_shot = True

            if self.charging_shot < 85:
                self.charging_shot = 0

            if self.charged_shot_enabled:
                new_shot = DinoShot((Camera, DinoShotGroup), (self.rect.centerx, self.shot_y_position), self.sprites_direction, 'big')
                self.charged_shot_enabled = False
                self.charging_shot = 0


    def gravity(self):
        if not self.stop_gravity:

            if self.gravity_force >= self.gravity_force_limit:
                self.lock_gravity_force = True

            if not self.lock_gravity_force:
                self.gravity_force += 0.4

            self.rect.y += self.gravity_force


    def blink_while_standing(self, key):
        if key[pygame.K_UP] and not key[pygame.K_DOWN]:
            self.current_blink_sprite = 0
            return

        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
            animation_list = [self.standing_sprite, self.standing_blink_sprite]

            if key[pygame.K_DOWN]:
                animation_list = [self.crouch_stopped_sprite, self.crouch_stopped_blink_sprite]

            self.current_blink_sprite += 0.002

            if self.current_blink_sprite >= len(animation_list)-0.99:
                self.current_blink_sprite = 0

            self.image = pygame.image.load(animation_list[int(self.current_blink_sprite)])

        else:
            self.current_blink_sprite = 0


    def dead(self):
        if self.life <= 0:
            self.image = pygame.image.load(self.die_sprite)


    def took_damage(self):
        if self.damage:
            self.life_timer -= 1.8
            if self.life_timer <= 0:
                self.life_timer = 75
                self.damage = False

            animation_list = self.took_damage_sprites
            self.current_damaged_sprite += 0.2
            if self.current_damaged_sprite >= len(animation_list):
                self.current_damaged_sprite = 0
            self.image = pygame.image.load(animation_list[int(self.current_damaged_sprite)])

            self.enable_dino_actions = False
            self.charged_shot_enabled = False
            self.charging_shot = 0
        else:
            self.enable_dino_actions = True


    def life_management(self):
        if self.life > 100:
            self.life = 100

        self.life_bar.size = (self.life * 1.82, 28)

        pygame.draw.rect(Camera.display_surface, (198, 0, 0), self.life_bar)
        Camera.display_surface.blit(self.life_dial, (20, 20))


    def update(self, *args):
        key = pygame.key.get_pressed()

        self.reload_sprites()
        self.dead()

        if not self.life <= 0:
            if self.enable_dino_actions:
                self.walk(key)
                self.jump(key)
                self.crouch(key)
                self.shot(key)

            self.walking_animation(key)
            self.gravity()
            self.blink_while_standing(key)
            self.took_damage()
            self.life_management()
