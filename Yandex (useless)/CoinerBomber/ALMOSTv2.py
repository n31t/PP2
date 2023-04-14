import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
PLAYER_SIZE = 50
COIN_SIZE = 30
BOMB_SIZE = 40
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GAME_DURATION = 12  # IN SECONDS
# game score and etc
red_team_score = 0
blue_team_score = 0
start_time = pygame.time.get_ticks()

# Initialize pygame
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Capture")
clock = pygame.time.Clock()

# Create players, coin, and bomb
player_red = pygame.Rect(50, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
player_blue = pygame.Rect(WIDTH - 50 - PLAYER_SIZE,
                          HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
coin = pygame.Rect(WIDTH // 2 - COIN_SIZE // 2, HEIGHT //
                   2 - COIN_SIZE // 2, COIN_SIZE, COIN_SIZE)
bomb = pygame.Rect(random.randint(100, WIDTH - 100),
                   random.randint(100, HEIGHT - 100), BOMB_SIZE, BOMB_SIZE)

# Flags for carrying coins and bombs
carrying_coin_red = False
carrying_coin_blue = False
carrying_bomb_red = False
carrying_bomb_blue = False

# Game timer
game_timer = pygame.time.get_ticks() + GAME_DURATION * 1000

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    # Update player movement
    if keys[pygame.K_w]:
        player_red.y -= 5
    if keys[pygame.K_s]:
        player_red.y += 5
    if keys[pygame.K_a]:
        player_red.x -= 5
    if keys[pygame.K_d]:
        player_red.x += 5

    if keys[pygame.K_UP]:
        player_blue.y -= 5
    if keys[pygame.K_DOWN]:
        player_blue.y += 5
    if keys[pygame.K_LEFT]:
        player_blue.x -= 5
    if keys[pygame.K_RIGHT]:
        player_blue.x += 5
    # Keep players within the window boundaries
    player_red.clamp_ip(win.get_rect())
    player_blue.clamp_ip(win.get_rect())

    # Check for collisions with coins
    if player_red.colliderect(coin):
        if not carrying_coin_red:
            carrying_coin_red = True
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)

    if player_blue.colliderect(coin):
        if not carrying_coin_blue:
            carrying_coin_blue = True
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)

    # Check for collisions with bombs
    if player_red.colliderect(bomb):
        if not carrying_bomb_red:
            carrying_bomb_red = True
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)

    if player_blue.colliderect(bomb):
        if not carrying_bomb_blue:
            carrying_bomb_blue = True
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)

        # Check for reaching the nests
    red_nest = pygame.Rect(0, HEIGHT // 2 - PLAYER_SIZE //
                           2, PLAYER_SIZE, PLAYER_SIZE)
    blue_nest = pygame.Rect(WIDTH - PLAYER_SIZE, HEIGHT //
                            2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)

    if player_red.colliderect(red_nest):
        if carrying_coin_red:
            carrying_coin_red = False
            # Deposit the coin in red team's box
            coin.x = WIDTH // 4 - COIN_SIZE // 2
            coin.y = HEIGHT // 2 - COIN_SIZE // 2
            red_team_score += 1
            # Add score for red team
            # Update the score for red team

        if carrying_bomb_red:
            carrying_bomb_red = False
            # Deposit the bomb in red team's box
            bomb.x = WIDTH // 4 - BOMB_SIZE // 2
            bomb.y = HEIGHT // 2 - BOMB_SIZE // 2
            red_team_score -= 3
            # Subtract score for red team
            # Update the score for red team
    ''''Imposter'''
    if player_red.colliderect(blue_nest):
        if carrying_coin_red:
            carrying_coin_red = False
            coin.x = WIDTH // 4 - COIN_SIZE // 2
            coin.y = HEIGHT // 2 - COIN_SIZE // 2
            blue_team_score += 1

        if carrying_bomb_red:
            carrying_bomb_red = False
            bomb.x = WIDTH // 4 - BOMB_SIZE // 2
            bomb.y = HEIGHT // 2 - BOMB_SIZE // 2
            blue_team_score -= 3

    ''''Imposter'''
    if player_blue.colliderect(red_nest):
        if carrying_coin_blue:
            carrying_coin_blue = False
            coin.x = WIDTH // 4 - COIN_SIZE // 2
            coin.y = HEIGHT // 2 - COIN_SIZE // 2
            red_team_score += 1

        if carrying_bomb_blue:
            carrying_bomb_blue = False
            bomb.x = WIDTH // 4 - BOMB_SIZE // 2
            bomb.y = HEIGHT // 2 - BOMB_SIZE // 2
            red_team_score -= 3

    if player_blue.colliderect(blue_nest):
        if carrying_coin_blue:
            carrying_coin_blue = False
            # Deposit the coin in blue team's box
            coin.x = WIDTH // 4 * 3 - COIN_SIZE // 2
            coin.y = HEIGHT // 2 - COIN_SIZE // 2
            blue_team_score += 1
            # Add score for blue team
            # Update the score for blue team

        if carrying_bomb_blue:
            carrying_bomb_blue = False
            # Deposit the bomb in blue team's box
            bomb.x = WIDTH // 4 * 3 - BOMB_SIZE // 2
            bomb.y = HEIGHT // 2 - BOMB_SIZE // 2
            blue_team_score -= 3
            # Subtract score for blue team
            # Update the score for blue team

    # Draw the game objects
    win.fill(BLACK)
    font = pygame.font.SysFont(None, 36)
    text_red = font.render("Red Team: {}".format(red_team_score), True, RED)
    text_blue = font.render(
        "Blue Team: {}".format(blue_team_score), True, BLUE)
    win.blit(text_red, (20, 20))
    win.blit(text_blue, (WIDTH - text_blue.get_width() - 20, 20))

    pygame.draw.rect(win, RED, player_red)
    pygame.draw.rect(win, BLUE, player_blue)
    pygame.draw.ellipse(win, YELLOW, coin)
    pygame.draw.rect(win, YELLOW, red_nest)
    pygame.draw.rect(win, YELLOW, blue_nest)
    pygame.draw.rect(win, RED, bomb)
    pygame.display.update()

    # Draw timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, GAME_DURATION - elapsed_time)
    timer_text = font.render(
        "Time Remaining: {} seconds".format(remaining_time), True, YELLOW)
    win.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 10))

    # Check for game over
    if remaining_time <= 0:
        winner = "Red" if red_team_score > blue_team_score else "Blue" if blue_team_score > red_team_score else "No one (Tie)"
        result_text = font.render(
            "Game Over! Winner: {}".format(winner), True, BLACK)
        win.blit(result_text, (WIDTH // 2 - 150, HEIGHT // 2 - 25))
        pygame.display.flip()

    # Limit frames per second
    pygame.display.update()
    clock.tick(60)
