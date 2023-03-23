import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
clock1 = pygame.image.load("main-clock.png")


def blitRotate(surf, image, pos, originPos, angle):

    # offset from pivot to center
    image_rect = image.get_rect(
        topleft=(pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x,
                            pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


image = pygame.image.load('left-hand.png')
image2 = pygame.image.load('right-hand.png')
w, h = image.get_size()
w2, h2 = image2.get_size()
angle = 0
angle2 = 0
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width()/2, screen.get_height()/2)
    screen.fill((255, 255, 255))
    screen.blit(clock1, (0, 0))
    blitRotate(screen, image, pos, (w/2, h/2), angle)
    blitRotate(screen, image2, pos, (w2/2, h2/2), angle2)
    angle -= 0.1
    angle2 += 0.0016161616161616
    pygame.display.flip()

pygame.quit()
exit()
