import pygame
from camera import CameraInit


pygame.init()


CollisionGroup = pygame.sprite.Group()
DinoShotGroup = pygame.sprite.Group()
MetalBallGroup = pygame.sprite.Group()
PterosaurGroup = pygame.sprite.Group()
HeartGroup = pygame.sprite.Group()
WaterGroup = pygame.sprite.Group()

Camera = CameraInit()
