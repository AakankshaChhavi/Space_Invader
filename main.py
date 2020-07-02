import pygame
import random
import math
from pygame import mixer
#initialise the pygame always
pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/ufo.png")
pygame.display.set_icon(icon)

bgimg = pygame.image.load("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/background.png")
bulletimg = pygame.image.load("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/bullet.png")

mixer.music.load("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/background.wav")
mixer.music.play(-1)#play on loop

score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
text_X = 10
text_Y = 10

def show_score(x,y):
    score = font.render("Score: "+str(score_val),True,(255,255,255))
    screen.blit(score,(x,y))


playerimg = pygame.image.load("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/arcade.png")
player_x = 370
player_y = 480
player_x_change = 0
def player(x,y):
    screen.blit(playerimg,(x,y))

enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 6
for i in range(num_of_enemy):
    enemy_img.append(pygame.image.load("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/spaceship.png"))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(5)
    enemy_y_change.append(40)
    
def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))

bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 20
bullet_state = "ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x+16,y+10))

def isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt(math.pow(enemy_x-bullet_x,2)+math.pow(enemy_y-bullet_y,2))
    if distance < 27:
        return True
    return False

game = pygame.font.Font("freesansbold.ttf",64)
def game_over_text():
    text = game.render("GAME OVER",True,(255,255,255))
    screen.blit(text,(200,250))


running = True
while running:
    screen.fill((4,50,60))
    screen.blit(bgimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            print("Keystroke is pressed")
            if event.key == pygame.K_LEFT:
                player_x_change = -5
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
                print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_x = player_x
                    bulle_sound = mixer.Sound("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/laser.wav")
                    bulle_sound.play()
                    fire_bullet(bullet_x,bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
                print("Keystroke has been released")
        
    player_x += player_x_change 
    if player_x <= 0:
        player_x = 0

    if player_x >= 736:
        player_x = 736 
    
    for i in range(num_of_enemy):  
        if enemy_y[i] > 440:
            for j in range(num_of_enemy):
                enemy_y[j] = 2000
            game_over_text()
            
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 5
            enemy_y[i]  += enemy_y_change[i]
        elif enemy_x[i] >= 736: 
            enemy_x_change[i] = -5
            enemy_y[i] += enemy_y_change[i]
        if isCollision(enemy_x[i],enemy_y[i],bullet_x,bullet_y):
            bullet_y = 480
            bullet_state = "ready"
            score_val += 1
            enemy_x[i] = random.randint(0,735)
            enemy_y[i] = random.randint(50,150)
            exlposion_sound = mixer.Sound("c:/Users/Aakanksha Chhavi/Desktop/Space_Invader/explosion.wav")
            exlposion_sound.play()
        enemy(enemy_x[i],enemy_y[i],i)
        
    player(player_x,player_y)
    
    
    if bullet_y <= 0:
        bullet_state = "ready"
        bullet_y = 480
    
    if bullet_state is "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change
    
    show_score(text_X,text_Y)
    
    
    pygame.display.update()  
      


