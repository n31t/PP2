import pygame
import random

# Define game constants
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COIN_SPAWN_INTERVAL = 120
GAME_DURATION = 120

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Carry Game")
clock = pygame.time.Clock()

# Load game assets
# Replace with actual image file
player_red = pygame.image.load("player_red.png")

# Replace with actual image file
player_blue = pygame.image.load("player_blue.png")

coin_image = pygame.image.load("coin.png")  # Replace with actual image file

bomb_image = pygame.image.load("bomb.png")  # Replace with actual image file

# Scale Game Assets
player1_image = pygame.transform.scale(player_red, (50, 50))
player2_image = pygame.transform.scale(player_blue, (50, 50))
coin_image = pygame.transform.scale(coin_image, (50, 50))
bomb_image = pygame.transform.scale(bomb_image, (50, 50))

player_red_rect = player1_image.get_rect()
player_red_rect.x = WIDTH // 2 - player_red_rect.width // 2
player_red_rect.y = 50

player_blue_rect = player2_image.get_rect()
player_blue_rect.x = WIDTH // 2 - player_blue_rect.width // 2
player_blue_rect.y = HEIGHT - player_blue_rect.height - 50

coin_rect = coin_image.get_rect()
coin_rect.x = random.randint(100, WIDTH - 100)
coin_rect.y = random.randint(100, HEIGHT - 100)

bomb_rect = bomb_image.get_rect()
bomb_rect.x = random.randint(100, WIDTH - 100)
bomb_rect.y = random.randint(100, HEIGHT - 100)

# Initialize game state
red_score = 0
blue_score = 0
timer = 0
carrying_coin_red = False
carrying_bomb_red = False
carrying_coin_blue = False
carrying_bomb_blue = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Update game timer
    timer += 1
    if timer >= COIN_SPAWN_INTERVAL:
        coin_rect.x = random.randint(100, WIDTH - 100)
        coin_rect.y = random.randint(100, HEIGHT - 100)
        bomb_rect.x = random.randint(100, WIDTH - 100)
        bomb_rect.y = random.randint(100, HEIGHT - 100)
        timer = 0

    # Draw game objects
    screen.fill(WHITE)
    screen.blit(player1_image, player_red_rect)
    screen.blit(player2_image, player_blue_rect)
    screen.blit(coin_image, coin_rect)
    screen.blit(bomb_image, bomb_rect)
    pygame.display.flip()
    clock.tick(60)

    # Update player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_red_rect.y -= 5
    if keys[pygame.K_s]:
        player_red_rect.y += 5
    if keys[pygame.K_a]:
        player_red_rect.x -= 5
    if keys[pygame.K_d]:
        player_red_rect.x += 5

    if keys[pygame.K_UP]:
        player_blue_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_blue_rect.y += 5
    if keys[pygame.K_LEFT]:
        player_blue_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_blue_rect.x += 5

    # Check for collisions with coins
    if player_red_rect.colliderect(coin_rect):
        if not carrying_coin_red:
            red_score += 1
            carrying_coin_red = True
            coin_rect.x = random.randint(100, WIDTH - 100)
            coin_rect.y = random.randint(100, HEIGHT - 100)

    if player_blue_rect.colliderect(coin_rect):
        if not carrying_coin_blue:
            blue_score += 1
            carrying_coin_blue = True
            coin_rect.x = random.randint(100, WIDTH - 100)
            coin_rect.y = random.randint(100, HEIGHT - 100)

    # Check for collisions with bombs
    if player_red_rect.colliderect(bomb_rect):
        if not carrying_bomb_red:
            red_score -= 1
            carrying_bomb_red = True
            bomb_rect.x = random.randint(100, WIDTH - 100)
            bomb_rect.y = random.randint(100, HEIGHT - 100)

    if player_blue_rect.colliderect(bomb_rect):
        if not carrying_bomb_blue:
            blue_score -= 1
            carrying_bomb_blue = True
            bomb_rect.x = random.randint(100, WIDTH - 100)
            bomb_rect.y = random.randint(100, HEIGHT - 100)

    # Check for reaching the nests
    if carrying_coin_red and player_red_rect.colliderect(coin_rect):
        carrying_coin_red = False

    if carrying_bomb_red and player_red_rect.colliderect(bomb_rect):
        carrying_bomb_red = False

    if carrying_coin_blue and player_blue_rect.colliderect(coin_rect):
        carrying_coin_blue = False

    if carrying_bomb_blue and player_blue_rect.colliderect(bomb_rect):
        carrying_bomb_blue = False

    # Check for game over
    if pygame.time.get_ticks() >= GAME_DURATION * 1000:
        pygame.quit()
        print("Game over!")
        print("Red team score:", red_score)
        print("Blue team score:", blue_score)
        break
