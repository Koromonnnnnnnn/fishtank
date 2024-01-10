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

goldfish = pygame.image.load('goldfish.png')
goldfish = pygame.transform.scale(goldfish, (100, 100))

while not gameover:  # GAME LOOP############################################################
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            

    pygame.display.flip()
    screen.fill((0, 0, 0))
