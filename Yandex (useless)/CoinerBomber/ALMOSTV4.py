import pygame
import random
import time

# Constants
WIDTH = 1000
HEIGHT = 800
PLAYER_SIZE = 50
NEST_SIZE = 60
COIN_SIZE = 30
BOMB_SIZE = 40
POTION_SIZE = 30
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GAME_DURATION = 60  # seconds
SPEED_R = 4
SPEED_B = 4
REGULAR_SPEED = 4
POTION_SPAWN = False
POTION_DURATION_R = False
POTION_DURATION_B = False
DEAD_B = False
DEAD_R = False

# game score and etc
red_team_score = 0
blue_team_score = 0
start_time = pygame.time.get_ticks()

# Initialize pygame
pygame.init()
pygame.font.init
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Capture")
clock = pygame.time.Clock()

# Create players, coin, and bomb
player_red = pygame.Rect(70, HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
player1_image = pygame.image.load("player_red.png")
player1_image = pygame.transform.scale(
    player1_image, (PLAYER_SIZE, PLAYER_SIZE))
player_blue = pygame.Rect(WIDTH - 70 - PLAYER_SIZE,
                          HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
player2_image = pygame.image.load("player_blue.png")
player2_image = pygame.transform.scale(
    player2_image, (PLAYER_SIZE, PLAYER_SIZE))
coin = pygame.Rect(WIDTH // 2 - COIN_SIZE // 2, HEIGHT //
                   2 - COIN_SIZE // 2, COIN_SIZE, COIN_SIZE)
coin_image = pygame.image.load("coin-2.png")
coin_image = pygame.transform.scale(
    coin_image, (COIN_SIZE, COIN_SIZE))
bomb = pygame.Rect(random.randint(100, WIDTH - 100),
                   random.randint(100, HEIGHT - 100), BOMB_SIZE, BOMB_SIZE)
bomb_image = pygame.image.load("bomb.png")
bomb_image = pygame.transform.scale(
    bomb_image, (BOMB_SIZE, BOMB_SIZE))
potion = pygame.Rect(random.randint(100, WIDTH - 100),
                     random.randint(100, HEIGHT - 100), POTION_SIZE, POTION_SIZE)
potion_image = pygame.image.load("fast.png")
potion_image = pygame.transform.scale(
    potion_image, (POTION_SIZE, POTION_SIZE))


# Background
BACKGROUND = pygame.image.load("map2.jpg")
BACKGROUND = pygame.transform.scale(
    BACKGROUND, (1000, 800))
BACKGROUND_RECT = pygame.Rect(0, 0, 1000, 800)
# Flags for carrying coins and bombs
carrying_coin_red = False
carrying_coin_blue = False
carrying_bomb_red = False
carrying_bomb_blue = False

# Game timer
timer_current = 0
timer_duration = 0
timer_duration2 = 0
timer_potion_duration = 0
timer_potion_spawn = 0
game_timer = pygame.time.get_ticks() + GAME_DURATION * 1000

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    # Music
    if (timer_current == 0):
        MAIN_THEME = pygame.mixer.Sound('music.mp3')
        MAIN_THEME.set_volume(0.3)
        MAIN_THEME.play()
    # Update player movement
    if keys[pygame.K_w]:
        player_red.y -= SPEED_R
    if keys[pygame.K_s]:
        player_red.y += SPEED_R
    if keys[pygame.K_a]:
        player_red.x -= SPEED_R
    if keys[pygame.K_d]:
        player_red.x += SPEED_R

    if keys[pygame.K_UP]:
        player_blue.y -= SPEED_B
    if keys[pygame.K_DOWN]:
        player_blue.y += SPEED_B
    if keys[pygame.K_LEFT]:
        player_blue.x -= SPEED_B
    if keys[pygame.K_RIGHT]:
        player_blue.x += SPEED_B
    # Keep players within the window boundaries
    player_red.clamp_ip(win.get_rect())
    player_blue.clamp_ip(win.get_rect())

    # Check for collisions with coins
    if player_red.colliderect(coin) and carrying_bomb_red == False:
        if not carrying_coin_red:
            carrying_coin_red = True
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)

    if player_blue.colliderect(coin) and carrying_bomb_blue == False:
        if not carrying_coin_blue:
            carrying_coin_blue = True
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)

    # Check for collisions with bombs
    if player_red.colliderect(bomb) and carrying_coin_red == False:
        if not carrying_bomb_red:
            carrying_bomb_red = True
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)

    if player_blue.colliderect(bomb) and carrying_coin_blue == False:
        if not carrying_bomb_blue:
            carrying_bomb_blue = True
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)
    # Collision with players AKA drop and kill system

    timer_current = pygame.time.get_ticks()  # Current time
    # Dead Recovery for blue
    if (timer_duration2 - timer_current) <= 0 and DEAD_B == True:
        SPEED_B = 4
        DEAD_B = False
    # Dead Recovery for red
    if (timer_duration - timer_current) <= 0 and DEAD_R == True:
        SPEED_R = 4
        DEAD_R = False
    # Potion recovery
    if (timer_potion_spawn - timer_current) <= 0 and POTION_SPAWN == True:
        POTION_SPAWN = False
        potion.x = random.randint(100, WIDTH - 100)
        potion.y = random.randint(100, HEIGHT - 100)

    # Potion duration
    if (timer_potion_duration - timer_current) <= 0 and POTION_DURATION_R == True:
        SPEED_R = 4
        POTION_DURATION_R == False
    if (timer_potion_duration - timer_current) <= 0 and POTION_DURATION_B == True:
        SPEED_B = 4
        POTION_DURATION_B == False

    # For both
    if player_red.colliderect(player_blue) and (carrying_coin_red == True or carrying_bomb_red == True) and (carrying_coin_blue == True or carrying_bomb_blue == True):
        carrying_coin_blue = False
        carrying_bomb_blue = False
        timer_duration2 = timer_current + 4000
        SPEED_B = 0
        DEAD_B = True
        sound = pygame.mixer.Sound('crash.mp3')
        sound.set_volume(0.04)
        sound.play()
        player_blue.x = WIDTH - 70 - PLAYER_SIZE
        player_blue.y = HEIGHT // 2
        carrying_coin_red = False
        carrying_bomb_red = False
        timer_duration = timer_current + 4000
        SPEED_R = 0
        DEAD_R = True
        player_red.x = 70
        player_red.y = HEIGHT // 2
    # For Red
    if player_red.colliderect(player_blue) and (carrying_coin_blue == True or carrying_bomb_blue == True):
        carrying_coin_blue = False
        carrying_bomb_blue = False
        timer_duration2 = timer_current + 4000
        SPEED_B = 0
        DEAD_B = True
        sound = pygame.mixer.Sound('crash.mp3')
        sound.set_volume(0.04)
        sound.play()
        player_blue.x = WIDTH - 70 - PLAYER_SIZE
        player_blue.y = HEIGHT // 2
    # For blue
    if player_blue.colliderect(player_red) and (carrying_coin_red == True or carrying_bomb_red == True):
        carrying_coin_red = False
        carrying_bomb_red = False
        timer_duration = timer_current + 4000
        SPEED_R = 0
        DEAD_R = True
        sound = pygame.mixer.Sound('crash.mp3')
        sound.set_volume(0.04)
        sound.play()
        player_red.x = 70
        player_red.y = HEIGHT // 2
    '''Features (potions)'''
    # Check for collisions with potions
    if player_red.colliderect(potion):
        #     potion.x = random.randint(100, WIDTH - 100)
        #     potion.y = random.randint(100, HEIGHT - 100)
        potion.x = 800
        potion.y = 800
        SPEED_R = 7
        POTION_SPAWN = True
        POTION_DURATION_R = True
        timer_potion_duration = timer_current + 3000
        timer_potion_spawn = timer_current + 7000
    if player_blue.colliderect(potion):
        #     potion.x = random.randint(100, WIDTH - 100)
        #     potion.y = random.randint(100, HEIGHT - 100)
        potion.x = 9999
        potion.y = 9999
        SPEED_B = 7
        POTION_SPAWN = True
        POTION_DURATION_B = True
        timer_potion_duration = timer_current + 3000
        timer_potion_spawn = timer_current + 7000

    # Check for reaching the nests
    red_nest = pygame.Rect(0, HEIGHT // 2 - NEST_SIZE //
                           2, NEST_SIZE, NEST_SIZE)
    blue_nest = pygame.Rect(WIDTH - NEST_SIZE, HEIGHT //
                            2 - NEST_SIZE // 2, NEST_SIZE, NEST_SIZE)

    if player_red.colliderect(red_nest):
        if carrying_coin_red:
            carrying_coin_red = False
            # Deposit the coin in red team's box
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)
            red_team_score += 1
            # Add score for red team
            # Update the score for red team

        if carrying_bomb_red:
            carrying_bomb_red = False
            # Deposit the bomb in red team's box
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)
            red_team_score -= 2
            # Subtract score for red team
            # Update the score for red team
    ''''Imposter'''
    if player_red.colliderect(blue_nest):
        if carrying_coin_red:
            carrying_coin_red = False
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)
            blue_team_score += 1

        if carrying_bomb_red:
            carrying_bomb_red = False
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)
            blue_team_score -= 2

    ''''Imposter'''
    if player_blue.colliderect(red_nest):
        if carrying_coin_blue:
            carrying_coin_blue = False
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)
            red_team_score += 1

        if carrying_bomb_blue:
            carrying_bomb_blue = False
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)
            red_team_score -= 2

    if player_blue.colliderect(blue_nest):
        if carrying_coin_blue:
            carrying_coin_blue = False
            # Deposit the coin in blue team's box
            coin.x = random.randint(100, WIDTH - 100)
            coin.y = random.randint(100, HEIGHT - 100)
            blue_team_score += 1
            # Add score for blue team
            # Update the score for blue team

        if carrying_bomb_blue:
            carrying_bomb_blue = False
            # Deposit the bomb in blue team's box
            bomb.x = random.randint(100, WIDTH - 100)
            bomb.y = random.randint(100, HEIGHT - 100)
            blue_team_score -= 2
            # Subtract score for blue team
            # Update the score for blue team
    # Draw the game objects
    win.blit(BACKGROUND, BACKGROUND_RECT)
    '''win.fill(BLACK)'''
    font = pygame.font.SysFont(None, 36)
    text_red = font.render("Arnur: {}".format(red_team_score), True, RED)
    text_blue = font.render(
        "Trump: {}".format(blue_team_score), True, BLUE)
    win.blit(text_red, (20, 20))
    win.blit(text_blue, (WIDTH - text_blue.get_width() - 20, 20))

    # pygame.draw.rect(win, RED, player_red)'''
    win.blit(player1_image, player_red)
    '''pygame.draw.rect(win, BLUE, player_blue)'''
    win.blit(player2_image, player_blue)
    pygame.draw.ellipse(win, YELLOW, coin)
    pygame.draw.rect(win, RED, red_nest)
    pygame.draw.rect(win, BLUE, blue_nest)
    pygame.draw.rect(win, RED, bomb)
    pygame.draw.rect(win, BLUE, potion)
    pygame.display.update()

    # Check for game over
    if pygame.time.get_ticks() >= game_timer:
        if red_team_score > blue_team_score:
            print("Red wins!")
        elif blue_team_score > red_team_score:
            print("Blue wins!")
        else:
            print("It's a tie!")
        pygame.quit()
    # Draw timer
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(0, GAME_DURATION - elapsed_time)
    timer_text = font.render(
        "Time Remaining: {} seconds".format(remaining_time), True, YELLOW)
    win.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, 30))
    # Limit frames per second
    pygame.display.update()
    clock.tick(60)
