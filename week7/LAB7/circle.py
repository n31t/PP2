import pygame
import random


def main():
    width = 900
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Circle')
    x = 50
    y = 50
    rad = 25
    vel = 10
    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - vel > 25:
            y -= vel
        if pressed[pygame.K_DOWN] and y + vel < 575:
            y += vel
        if pressed[pygame.K_LEFT] and x - vel > 25:
            x -= vel
        if pressed[pygame.K_RIGHT] and x + vel < 875:
            x += vel

        screen.fill((255, 255, 255))
        pygame.draw.circle(
            screen, (random.randint(0, 100), random.randint(0, 100), random.randint(0, 75)), (x, y), rad, 0)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
