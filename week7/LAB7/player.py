import pygame
pygame.init()
pygame.font.init()
f1 = pygame.font.Font(None, 24)
x = 0
W = 800
H = 600

screen = pygame.display.set_mode((W, H))
screen.fill((0, 180, 255))
text1 = f1.render('Press \'SPACEBAR\' to stop or play music', True,
                  (255, 255, 255))
text2 = f1.render('Press \'>\' or \'<\' for next or previous track', True,
                  (255, 255, 255))
screen.blit(text1, (10, 500))
screen.blit(text2, (10, 550))
pygame.display.update()
songs = ["liluziv.mp3", "uzi2.mp3",
         "prada24k.mp3", "laroi.mp3"]
pics = ["liluziv.jpg", "uzi2.jpeg",
        "prada24k.jpeg", "laroi.jpeg"]
pygame.mixer.music.load(songs[x])
start = False
stop = True
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                if stop == True:
                    if start == False:
                        pygame.mixer.music.play()
                        start = True
                        cov = pygame.image.load(pics[x]).convert()
                        cover = pygame.transform.scale(cov, (350, 350))
                        image = cover.get_rect(center=(W/2, H/3))
                        screen.blit(cover, image)
                    else:
                        pygame.mixer.music.unpause()
                    stop = False
                else:
                    pygame.mixer.music.pause()
                    stop = True
            if pressed[pygame.K_LEFT]:
                if x != 0:
                    x -= 1
                else:
                    x = len(songs)-1
                cov = pygame.image.load(pics[x]).convert()
                cover = pygame.transform.scale(cov, (350, 350))
                image = cover.get_rect(center=(W/2, H/3))
                screen.blit(cover, image)
                pygame.mixer.music.load(songs[x])
                pygame.mixer.music.play()
            if pressed[pygame.K_RIGHT]:
                if x != len(songs)-1:
                    x += 1
                else:
                    x = 0
                cov = pygame.image.load(pics[x]).convert()
                cover = pygame.transform.scale(cov, (350, 350))
                image = cover.get_rect(center=(W/2, H/3))
                screen.blit(cover, image)
                pygame.mixer.music.load(songs[x])
                pygame.mixer.music.play()
        pygame.display.update()
