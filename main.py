import pygame
import random
from pygame import mixer

pygame.init()
mixer.init()

pygame.display.set_caption("Fishtank")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
gameover = False


eel = pygame.image.load('eel.png')
eel = pygame.transform.scale(eel, (100, 100))

goldfish = pygame.image.load('goldfish.png')
goldfish = pygame.transform.scale(goldfish, (100, 100))

clownfish = pygame.image.load('clownfish.png')
clownfish = pygame.transform.scale(clownfish, (100, 100))

starfish = pygame.image.load('starfish.png')
starfish = pygame.transform.scale(starfish, (100, 100))

while not gameover:  
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
         
    screen.blit(eel, (500, 500))
    screen.blit(goldfish, (400,400))
    screen.blit(clownfish, (200, 200))
    screen.blit(starfish, (100, 100))
    
    pygame.display.flip()
    screen.fill((0, 0, 0))
