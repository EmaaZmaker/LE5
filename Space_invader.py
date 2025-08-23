import pygame
import math
import random

#constant

screen_width=800
screen_height=500
player_start_x=370
player_start_y=380
enemy_start_y_min=50
enemy_start_y_max=150
enemy_speed_x=4
enemy_speed_y=40
bullet_speed_y=10
collsion_distance=27

pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))

background=pygame.image.load("background.png")

#caption & icon

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

#player

player_image=pygame.image.load("player.png")
player_x=player_start_x
player_y=player_start_y
player_x_change=0

#intsilising enemy variable
enemy_image=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
number_of_enemies=6

#creating enemies
for _i in range(number_of_enemies):
    enemy_image.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0,screen_width-64))
    enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

#bullet
bullet_image=pygame.image.load("bullet.png")
bullet_x=0
bullet_y=player_start_y
bullet_x_change=0
bullet_y_change=bullet_speed_y
bullet_state="ready"

#score value
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
text_x=10
text_y=10

#game over text
over_font=pygame.font.Font("freesansbold.ttf",64)

#displaying current score on screen 
def show_score(x,y):
    score=font.render("score"+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

#display game over etxt
def game_over_text():
    over_text=font.render("game over!",True,(255,255,255))
    screen.blit(over_text,(200,250))
#drawing player on screen
def player(x,y):
    screen.blit(player_image,(x,y))

#draw enemy on screen
def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))

#function to fire bullet
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_image,(x+16,y+10))
#check collision between enemy & bullet
def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):

# Check if there is a collision between the enemy and a bullet

    distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)

    return distance < collsion_distance