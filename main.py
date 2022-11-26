def main():
    while True:
        pygame.time.Clock().tick(300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        update_collisions()

        SCREEN.fill((32, 32, 32))

        Camera.update()
        Camera.update_draw(dino)

        pygame.display.update()


if __name__ == '__main__':
    import sys, pygame

    from screen_size import SCREEN_WIDTH, SCREEN_HEIGHT

    pygame.init()

    pygame.display.set_caption('Mega Dino')
    pygame.display.set_icon(pygame.image.load('Images/Dino_(to_right)/dino_standing_damaged.png'))

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    from groups import *
    from collisions import update_collisions
    from sprites import dino

    main()
