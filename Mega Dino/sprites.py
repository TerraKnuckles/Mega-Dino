import pygame
from groups import *
from dino import Dino
from collision_box import CollisionBox
from pterosaur import Pterosaur
from map import GroundMap


pygame.init()


map = GroundMap(Camera)

platform0 = CollisionBox((Camera, CollisionGroup), (1134, 546), (168, 42))
platform1 = CollisionBox((Camera, CollisionGroup), (1008, 210), (336, 42))
platform2 = CollisionBox((Camera, CollisionGroup), (1470, 378), (168, 42))
platform3 = CollisionBox((Camera, CollisionGroup), (1470, 630), (168, 42))
platform4 = CollisionBox((Camera, CollisionGroup), (1680, 168), (168, 42))
platform5 = CollisionBox((Camera, CollisionGroup), (1806, 0), (210, 42))
platform6 = CollisionBox((Camera, CollisionGroup), (2352, 336), (210, 42))
platform7 = CollisionBox((Camera, CollisionGroup), (2352, 630), (210, 42))
platform8 = CollisionBox((Camera, CollisionGroup), (2142, 504), (168, 42))
platform9 = CollisionBox((Camera, CollisionGroup), (2688, 210), (252, 42))
platform10 = CollisionBox((Camera, CollisionGroup), (2856, 546), (168, 42))
platform11 = CollisionBox((Camera, CollisionGroup), (3108, 588), (168, 42))
platform12 = CollisionBox((Camera, CollisionGroup), (1554, 252), (84, 42))

brick_wall0 = CollisionBox((Camera, CollisionGroup), (3906, 420), (42, 672))
brick_wall1 = CollisionBox((Camera, CollisionGroup), (126, 420), (42, 672))

ground = CollisionBox((Camera, CollisionGroup), (714, 756), (2646, 42))

water0 = CollisionBox((Camera, WaterGroup), (168, 798), (546, 294))
water1 = CollisionBox((Camera, WaterGroup), (3360, 798), (546, 294))

dino = Dino(Camera)

pterosaur = Pterosaur((Camera, PterosaurGroup), (1000, 476), (dino))
