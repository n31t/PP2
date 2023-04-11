import pygame
pygame.init()

WEIGHT = 900
HEIGHT = 700
RADIUS = 30
# Making canvas
screen = pygame.display.set_mode((WEIGHT, HEIGHT))

# Setting Title
pygame.display.set_caption('Paint')

draw_on = False
last_pos = (0, 0)

ch_color = (255, 255, 255)

# Create a Font object
font = pygame.font.Font(None, 25)

# Messages to display
messages = ["E - eraser", "S - draw square", "M - draw right triangle", "C - draw circle", "R - draw rectangle", "H - draw rhombus", "Q - draw equilateral triangle",
            "B - color: blue", "Y - color: yellow", "P - color: purple", "T - Radius decreasing", "G - Radius increasing"]


def roundline(canvas, color, start, end, RADIUS=1):
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist):
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), RADIUS)


def draw_circle(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # Radius of the circle
    radius = RADIUS
    # Draw the circle on the screen
    pygame.draw.circle(screen, ch_color, pos, radius)


def draw_rect(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # The size of the rectangle
    rect_size = (80, 50)
    # The position of the top-left corner of the rectangle
    rect_pos = (pos[0] - rect_size[0]/2, pos[1] - rect_size[1]/2)
    # Draw the rectangle on the screen
    pygame.draw.rect(screen, ch_color, (rect_pos, rect_size))


def draw_square(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # The size of the rectangle
    s_size = (50, 50)
    # The position of the top-left corner of the rectangle
    s_pos = (pos[0] - s_size[0]/2, pos[1] - s_size[1]/2)
    # Draw the rectangle on the screen
    pygame.draw.rect(screen, ch_color, (s_pos, s_size))


def draw_right_triangle(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # Draw the rectangle on the screen
    pygame.draw.polygon(
        screen, ch_color, ((pos[0], pos[1]), (pos[0]+50, pos[1]), (pos[0], pos[1]-50)))


def draw_equilateral_triangle(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # Draw the rectangle on the screen
    pygame.draw.polygon(screen, ch_color, ((
        pos[0], pos[1]), (pos[0]+25, pos[1]+50), (pos[0]-25, pos[1]+50)))


def draw_rhombus(ch_color):
    # Get the current mouse position
    pos = pygame.mouse.get_pos()
    # Draw the rectangle on the screen
    pygame.draw.polygon(screen, ch_color, ((
        pos[0], pos[1]), (pos[0]+25, pos[1]+25), (pos[0], pos[1]+50), (pos[0]-25, pos[1]+25)))


try:
    while True:
        # Waiting for any action
        e = pygame.event.wait()

        if e.type == pygame.QUIT:
            raise StopIteration
        # Blit message on the screen
        for i, message in enumerate(messages):
            text_surface = font.render(message, True, (0, 100, 255))
            screen.blit(text_surface, (10, 10 + i * 40))

        # User action
        if e.type == pygame.KEYDOWN:
            if e.key == ord("p"):
                ch_color = (128, 0, 128)
            if e.key == ord("b"):
                ch_color = (0, 191, 255)
            if e.key == ord("y"):
                ch_color = (255, 255, 0)
            if e.key == ord("r"):
                draw_rect(ch_color)
            if e.key == ord("c"):
                draw_circle(ch_color)
            if e.key == ord("s"):
                draw_square(ch_color)
            if e.key == ord("m"):
                draw_right_triangle(ch_color)
            if e.key == ord("q"):
                draw_equilateral_triangle(ch_color)
            if e.key == ord("h"):
                draw_rhombus(ch_color)
            if e.key == ord("e"):
                ch_color = (0, 0, 0)
            if e.key == ord("t"):
                if (RADIUS != 0):
                    RADIUS = RADIUS - 1
            if e.key == ord("g"):
                RADIUS = RADIUS + 1

        if e.type == pygame.MOUSEBUTTONDOWN:
            # Chosen color
            color = ch_color
            # Draw a single circle wheneven mouse is clicked down.
            pygame.draw.circle(screen, color, e.pos, RADIUS-15)
            draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        # It will draw a continuous circle with the help of roundline functxfion.
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.draw.circle(screen, color, e.pos, RADIUS-15)
                roundline(screen, color, e.pos, last_pos, RADIUS-15)
            last_pos = e.pos
        pygame.display.flip()

except StopIteration:
    pass

# Quit
pygame.quit()
