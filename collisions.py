import pygame
from groups import *
from sprites import *


def dino_x_tile():
    collision_with_tile = pygame.sprite.spritecollide(dino, CollisionGroup, False)
    if collision_with_tile:
        for tile in collision_with_tile:
            # DINO TOUCH FLOOR
            if dino.rect.bottom <= tile.rect.top + 10:
                # GRAVITY PROPERTIES
                dino.stop_gravity = True
                dino.lock_gravity_force = False
                dino.gravity_force = 0

                # JUMP PROPERTIES
                dino.enable_jump = True
                dino.jump_force = 16

                dino.on_the_floor = True
                dino.rect.bottom = tile.rect.top + 10

            # DINO TOUCH ROOF
            if dino.rect.top >= tile.rect.top:
                # GRAVITY PROPERTIES
                dino.stop_gravity = False

                # JUMP PROPERTIES
                dino.jump_force = 0

                dino.on_the_floor = False

            # DINO TOUCH RIGHT WALL
            if dino.rect.left >= tile.rect.right - 10:
                if not dino.rect.bottom == tile.rect.top + 10:
                    dino.can_move_left = False
                    dino.rect.left = tile.rect.right - 8
            else:
                dino.can_move_left = True

            # DINO TOUCH LEFT WALL
            if dino.rect.right <= tile.rect.left + 16:
                if not dino.rect.bottom == tile.rect.top + 10:
                    dino.can_move_right = False
                    dino.rect.right = tile.rect.left + 14
            else:
                dino.can_move_right = True

    else:
        # GRAVITY PROPERTIES
        dino.stop_gravity = False

        # MOVEMENT PROPERTIES
        dino.can_move_left = True
        dino.can_move_right = True

        dino.on_the_floor = False


def dino_shot_x_pterosaur():
    dino_shot_collision_with_pterosaur = pygame.sprite.groupcollide(DinoShotGroup, PterosaurGroup, False, False)
    for (dino_shot, pterosaur) in dino_shot_collision_with_pterosaur.items():
        if pygame.sprite.collide_mask(dino_shot, pterosaur[0]):
            pterosaur[0].life -= dino_shot.damage
            dino_shot.kill()


def dino_x_pterosaur():
    collision_with_pterosaur = pygame.sprite.spritecollide(dino, PterosaurGroup, False)
    for pterosaur in collision_with_pterosaur:
        if pygame.sprite.collide_mask(dino, pterosaur) and dino.damage is False:
            dino.life -= 30
            dino.damage = True


def projectile_x_tile():
    metal_ball_collision = pygame.sprite.groupcollide(MetalBallGroup, CollisionGroup, True, False)

    dino_shot_collision = pygame.sprite.groupcollide(DinoShotGroup, CollisionGroup, False, False)
    for (dino_shot, tile) in dino_shot_collision.items():
        if abs(dino_shot.rect.left >= tile[0].rect.right) or abs(dino_shot.rect.right <= tile[0].rect.left):
            dino_shot.kill()


def dino_x_metal_ball():
    collision_with_metal_ball = pygame.sprite.spritecollide(dino, MetalBallGroup, False)
    for metal_ball in collision_with_metal_ball:
        if pygame.sprite.collide_mask(dino, metal_ball) and dino.damage is False:
            dino.life -= metal_ball.damage
            dino.damage = True
            metal_ball.kill()


def dino_x_heart():
    dino_collide_heart = pygame.sprite.spritecollide(dino, HeartGroup, False)
    for heart in dino_collide_heart:
        if pygame.sprite.collide_mask(dino, heart):
            dino.life += heart.cure
            heart.kill()


def heart_x_tile():
    heart_collide_tile = pygame.sprite.groupcollide(HeartGroup, CollisionGroup, False, False)
    for (heart, tile) in heart_collide_tile.items():

        if heart.rect.bottom <= tile[0].rect.top + 7:
            heart.rect.bottom = tile[0].rect.top


def dino_x_water():
    if pygame.sprite.spritecollide(dino, WaterGroup, False):
        dino.life = 0


def heart_x_water():
    heart_collide_water = pygame.sprite.groupcollide(HeartGroup, CollisionGroup, True, False)


def update_collisions():
    dino_x_tile()
    dino_shot_x_pterosaur()
    dino_x_pterosaur()
    projectile_x_tile()
    dino_x_metal_ball()
    dino_x_heart()
    heart_x_tile()
    dino_x_water()
    heart_x_water()
