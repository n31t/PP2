import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
GREEN = (124, 252, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
FONT_SIZE = 24

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Coin Collecting Game")

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load Game Assets
player1_image = pygame.image.load("player1.png")
player2_image = pygame.image.load("player2.png")
coin_image = pygame.image.load("coin.png")
bomb_image = pygame.image.load("bomb.png")
nest_image = pygame.image.load("nest.png")

# Scale Game Assets
player1_image = pygame.transform.scale(player1_image, (50, 50))
player2_image = pygame.transform.scale(player2_image, (50, 50))
coin_image = pygame.transform.scale(coin_image, (50, 50))
bomb_image = pygame.transform.scale(bomb_image, (50, 50))
nest_image = pygame.transform.scale(nest_image, (100, 100))

# Set Game Clock
clock = pygame.time.Clock()

# Set Initial Game State
player1_pos = [50, HEIGHT // 2]
player2_pos = [WIDTH - 100, HEIGHT // 2]
coin_pos = [WIDTH // 2, HEIGHT // 2]
bomb_pos = [WIDTH // 2, HEIGHT // 2]
player1_score = 0
player2_score = 0
game_start_time = pygame.time.get_ticks()
game_duration = 60000  # 1 minute in milliseconds
carrying_coin1 = False
carrying_coin2 = False
carrying_bomb1 = False
carrying_bomb2 = False
nest1_pos = [0, HEIGHT // 2 - 50]
nest2_pos = [WIDTH - 100, HEIGHT // 2 - 50]

# Set Font
font = pygame.font.SysFont(None, FONT_SIZE)

# Generate Random Map Borders
border_width = 100
border_height = 100
border_top_left = (border_width, border_height)
border_top_right = (WIDTH - border_width * 2, border_height)
border_bottom_left = (border_width, HEIGHT - border_height * 2)
border_bottom_right = (WIDTH - border_width * 2, HEIGHT - border_height * 2)

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Get Player1 Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos[1] -= 5
    if keys[pygame.K_s]:
        player1_pos[1] += 5
    if keys[pygame.K_a]:
        player1_pos[0] -= 5
    if keys[pygame.K_d]:
        player1_pos[0] += 5
    if keys[pygame.K_e]:
        if pygame.Rect(player1_pos[0], player1_pos[1], 50, 50).colliderect(pygame.Rect(bomb_pos[0], bomb_pos[1], 50, 50)):
            carrying_bomb1 = True

    # Get Player2 Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player2_pos[1] += 5
    if keys[pygame.K_LEFT]:
        player2_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player2_pos[0] += 5
    if keys[pygame.K_KP0]:
        if pygame.Rect(player2_pos[0], player2_pos[1], 50, 50).colliderect(pygame.Rect(coin_pos[0], coin_pos[1], 50, 50)):
            carrying_coin2 = True
    if keys[pygame.K_KP1]:
        if pygame.Rect(player2_pos[0], player2_pos[1], 50, 50).colliderect(pygame.Rect(bomb_pos[0], bomb_pos[1], 50, 50)):
            carrying_bomb2 = True

    # Update Player1 Score
    if carrying_coin1 and pygame.Rect(player1_pos[0], player1_pos[1], 50, 50).colliderect(pygame.Rect(nest1_pos[0], nest1_pos[1], 100, 100)):
        player1_score += 1
        carrying_coin1 = False

    # Update Player2 Score
    if carrying_coin2 and pygame.Rect(player2_pos[0], player2_pos[1], 50, 50).colliderect(pygame.Rect(nest2_pos[0], nest2_pos[1], 100, 100)):
        player2_score += 1
        carrying_coin2 = False

    # Update Player1 and Player2 Score with Bomb
    if carrying_bomb1 and pygame.Rect(player1_pos[0], player1_pos[1], 50, 50).colliderect(pygame.Rect(nest2_pos[0], nest2_pos[1], 100, 100)):
        player1_score -= 3
        carrying_bomb1 = False

    if carrying_bomb2 and pygame.Rect(player2_pos[0], player2_pos[1], 50, 50).colliderect(pygame.Rect(nest1_pos[0], nest1_pos[1], 100, 100)):
        player2_score -= 3
        carrying_bomb2 = False

    # Update Timer
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - game_start_time

    # Check if game time is over
    if elapsed_time >= game_duration:
        # End of Game
        game_over = True
        # End of Game Loop
        # Check and Display Winner
        winner = "Player 1" if player1_score > player2_score else "Player 2" if player2_score > player1_score else "No one (Tie)"
        result_text = font.render(
            "Game Over! Winner: {}".format(winner), True, BLACK)
        screen.blit(result_text, (WIDTH //
                                  2 - 150, HEIGHT // 2 - 25))
        pygame.display.flip()

        # Wait for 3 seconds
        pygame.time.delay(3000)

        # Quit Pygame
        pygame.quit()
    else:
        # Draw Game Objects
        # Draw Game Objects
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, pygame.Rect(
            border_top_left[0], border_top_left[1], border_top_right[0], border_bottom_left[1]), 2)
        pygame.draw.rect(screen, BLACK, pygame.Rect(
            border_top_left[0], border_top_left[1], border_bottom_left[0], border_bottom_right[1]), 2)
        pygame.draw.rect(screen, BLACK, pygame.Rect(
            border_top_right[0], border_top_right[1], border_bottom_right[0], border_bottom_right[1]), 2)
        pygame.draw.rect(screen, BLACK, pygame.Rect(
            border_bottom_left[0], border_bottom_left[1], border_bottom_right[0], border_bottom_right[1]), 2)

        pygame.draw.rect(screen, RED, pygame.Rect(
            player1_pos[0], player1_pos[1], 50, 50))
        pygame.draw.rect(screen, BLUE, pygame.Rect(
            player2_pos[0], player2_pos[1], 50, 50))

        pygame.draw.rect(screen, GREEN, pygame.Rect(
            nest1_pos[0], nest1_pos[1], 100, 100))
        pygame.draw.rect(screen, GREEN, pygame.Rect(
            nest2_pos[0], nest2_pos[1], 100, 100))

        pygame.draw.rect(screen, YELLOW, pygame.Rect(
            coin_pos[0], coin_pos[1], 50, 50))

        if carrying_coin1:
            pygame.draw.rect(screen, RED, pygame.Rect(
                player1_pos[0], player1_pos[1] - 30, 20, 20))
        if carrying_coin2:
            pygame.draw.rect(screen, BLUE, pygame.Rect(
                player2_pos[0], player2_pos[1] - 30, 20, 20))
        if carrying_bomb1:
            pygame.draw.rect(screen, RED, pygame.Rect(
                player1_pos[0], player1_pos[1] + 30, 20, 20))
        if carrying_bomb2:
            pygame.draw.rect(screen, BLUE, pygame.Rect(
                player2_pos[0], player2_pos[1] + 30, 20, 20))

        # Draw Scores and Timer
        score_text = font.render(
            "Player 1 Score: {}".format(player1_score), True, RED)
        screen.blit(score_text, (10, 10))
        score_text = font.render(
            "Player 2 Score: {}".format(player2_score), True, BLUE)
        screen.blit(score_text, (WIDTH - 200, 10))
        timer_text = font.render("Time Left: {} sec".format(
            (game_duration - elapsed_time) // 1000), True, BLACK)
        screen.blit(timer_text, (WIDTH // 2 - 100, 10))

        pygame.display.flip()
