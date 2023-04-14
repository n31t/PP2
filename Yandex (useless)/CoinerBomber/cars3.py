# Imports
import pygame
import sys
from pygame.locals import *
import random
import time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
YELLOW = (255, 191, 0)
BLUE = (0, 30, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCORE2 = 0
SCORE3 = 0  # ONLY FOR SPEED INC
COIN_VALUE = 0
COIN_RANDOMNESS = (random.randint(0, 100))

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")
background = pygame.transform.scale(background, (400, 600))
# Create a white screen
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Our coin class


class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        global COIN_VALUE
        global COIN_RANDOMNESS
        self.rect.move_ip(0, 5)
        # Gold 1 point coin
        if (COIN_RANDOMNESS < 50):
            self.image = pygame.image.load("coin.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            COIN_VALUE = 1
        # Silver 5 points coin
        elif (COIN_RANDOMNESS > 50 and COIN_RANDOMNESS != 100):
            self.image = pygame.image.load("coin2.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            COIN_VALUE = 5
        # Secret 1% coin
        elif (COIN_RANDOMNESS == 100):
            self.image = pygame.image.load("coin2.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            COIN_VALUE = 10
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
            COIN_RANDOMNESS = (random.randint(0, 100))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
       # if pressed_keys[K_UP]:
        # self.rect.move_ip(0, -5)
       # if pressed_keys[K_DOWN]:
        # self.rect.move_ip(0,5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(10, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Point()


# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


# Adding a new User event
# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:

    # Cycles through all events occurring
    for event in pygame.event.get():
        if SCORE3 == 10:
            SPEED += 3
            SCORE3 = 0
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    scores2 = font_small.render('Coins:' + str(SCORE2), True, YELLOW)
    DISPLAYSURF.blit(scores2, (SCREEN_WIDTH-130, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        sound = pygame.mixer.Sound('crash.mp3')
        sound.set_volume(0.02)
        sound.play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        f = pygame.font.Font(None, 100)
        scores = f.render('Good luck!', True, BLACK)
        DISPLAYSURF.blit(scores, (2, 300))
        # DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    # Coin pick up mechanic
    if pygame.sprite.spritecollideany(P1, coins):
        C1.rect.top = 0
        C1.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
        SCORE2 = SCORE2 + COIN_VALUE
        SCORE3 = SCORE3 + COIN_VALUE
        COIN_RANDOMNESS = (random.randint(0, 100))
        # I forget to find a good coin_pickup sound, so it is what it is
        # sound = pygame.mixer.Sound('coin_pickup.mp3')
    pygame.display.update()
    FramePerSec.tick(FPS)
