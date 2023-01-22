import pygame
import random

pygame.init()

gamescreen=pygame.display.set_mode((1000,750))

situation=True

#icon load and set location
monster=pygame.image.load("icon.png")
monster_location=monster.get_rect()
monster_location.topleft=(470,370)

#musics load and background music play
pygame.mixer.music.load("background_music.wav")
pygame.mixer.music.play(-1,0,0)
point_collect_sound = pygame.mixer.Sound("point_collect_sound.wav")
time_over = pygame.mixer.Sound("time_over.wav")

time = pygame.time.Clock()

#coin icon load and set location with random library
coin = pygame.image.load("dollar-coin.png")
coin_location = coin.get_rect()
coin_location.topleft = (random.randint(0,1000),random.randint(100,750))

background_image = pygame.image.load("backgraund.jpg")

font = pygame.font.SysFont("consolas",64)

score = 0
fps = 60
distance = 10
time_left = 10

while situation:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            situation=False

    gamescreen.blit(background_image,(0,0))
    gamescreen.blit(monster, monster_location)
    gamescreen.blit(coin, coin_location)

    #set timer for gameover
    ticks = pygame.time.get_ticks()
    timer = time_left-(int(ticks/1000))

    #set score text and draw line
    text = font.render("Score: "+str(score), True, (255,0,0))
    text_location = text.get_rect()
    text_location.topleft=(20,20)
    gamescreen.blit(text,text_location)
    pygame.draw.line(gamescreen,(255,0,0),(0,100),(1000,100),2)
    time_text = font.render("Time: "+str(timer), True, (255,0,0))
    time_text_location = time_text.get_rect()
    time_text_location.topleft= (700,20)
    gamescreen.blit(time_text,time_text_location)
    time.tick(fps)



    #what happens when the counter reaches zero
    if timer == 0:
        pygame.mixer.music.stop()
        gamescreen.fill((0,0,0))
        pygame.display.flip()
        time_over.play()
        text = font.render("Score: " + str(score), True, (255, 0, 0))
        text_location = text.get_rect()
        text_location.topleft = (350, 350)
        gamescreen.blit(text, text_location)
        time_text = font.render("Time: " + str(time_left), True, (255, 0, 0))
        time_text_location = time_text.get_rect()
        time_text_location.topleft = (350, 250)
        gamescreen.blit(time_text, time_text_location)
        pygame.display.update()
        pygame.time.wait(5000)
        situation=False

    #movement settings
    print(timer)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and monster_location.left>15:
        monster_location.x-=distance
    elif key[pygame.K_RIGHT] and monster_location.right<985:
        monster_location.x+=distance
    elif key[pygame.K_UP] and monster_location.top>115:
        monster_location.y-=distance
    elif key[pygame.K_DOWN] and monster_location.bottom<735:
        monster_location.y+=distance

    #they will be from the situation where the monster and gold collide
    if monster_location.colliderect(coin_location):
        point_collect_sound.play()
        coin_location.x=random.randint(0,968)
        coin_location.y=random.randint(101,718)
        score+=1
        time_left+=1

    pygame.display.update()
pygame.quit()