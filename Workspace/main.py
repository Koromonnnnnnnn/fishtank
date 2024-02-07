import pygame
import random
from pygame import mixer

from database import snail
from database import eel
from database import goldfish
from database import clownfish
from database import starfish

#HI EVERYBODY!!!!!!! LIVE SHARE IS WORKING!!!! -Gus & Daniel

pygame.init()
mixer.init()

pygame.display.set_caption("Fishtank")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
mixer.music.load('rave.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()
gameOver = False

# CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

vX = 0
vY = 0

keys = [False, False, False, False]

# ANIMATION
frameWidth = 64
frameHeight = 96
RowNum = 0  # for left animation
frameNum = 0
ticker = 0


frameWidth = 64
frameHeight = 96
RowNum = 1  # for Right animation
frameNum = 0
ticker = 0

frameWidth = 64
frameHeight = 96
RowNum = 2  # for Up animation
ticker = 0


frameWidth = 64
frameHeight = 96
RowNum = 3  # for Down animation
frameNum = 0
ticker = 0

# storing x,y values in a list for easier access
xvalues = [500, 700, 400, 200, 100]
yvalues = [500, 500, 400, 200, 100]

while not gameOver:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
            
    # Implemement random fish movement here

    
    # PHYSICS
    
    # LEFT MOVEMENT
    if keys[LEFT] == True:
        vX = -3
        direction = 0
        RowNum = 0

    # RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vX = 3
        direction = 1
        RowNum = 1

    # UP MOVEMENT
    elif keys[UP] == True:
        vY = -6
        direction = 2
        RowNum = 2

    # DOWN MOVEMENT
    elif keys[DOWN] == True:
        vY = 6
        direction = 3
        RowNum = 3

    # turn off velocity
    else:
        vX = 0

    # ANIMATION-------------------------------------------------------------------

    # Update Animation Information
    if vX < 0:  # left animation
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
        if frameNum > 7:
            frameNum = 0

    # Update Animation Information
    if vX > 0:  # Right animation
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
        if frameNum > 7:
            frameNum = 0

    # Update Animation Information
    if vY < 0:  # DOWN animation
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
        if frameNum > 7:
            frameNum = 0

    # Update Animation Information
    if vY > 0:  # UP animation
        ticker += 1
        if ticker % 10 == 0:  # only change frames every 10 ticks
            frameNum += 1
        if frameNum > 7:
            frameNum = 0

    # COLLISION HERE

    # RENDER SECTION
    screen.blit(snail, (xvalues[0], yvalues[0]))
    screen.blit(eel, (xvalues[1], yvalues[1]))
    screen.blit(goldfish, (xvalues[2], yvalues[2]))
    screen.blit(clownfish, (xvalues[3], yvalues[3]))
    screen.blit(starfish, (xvalues[4], yvalues[4]))

    pygame.display.flip()
    screen.fill((0, 0, 0))

if gameOver == True:
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over", True, WHITE)
    text_rect = text.get_rect(center=(800 // 2, 800 // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

    pygame.time.delay(1000)

    pygame.quit()
