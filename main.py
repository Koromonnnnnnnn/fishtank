import pygame
import random
from pygame import mixer

pygame.init()
mixer.init()

pygame.display.set_caption("Fishtank")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
mixer.music.load('rave.mp3')
mixer.music.set_volume(0.5)
mixer.music.play()
gameover = False

xvalues = [500, 700, 400, 200, 100]
yvalues = [500, 500, 400, 200, 100]

snail = pygame.image.load('snail.png')
snail = pygame.transform.scale(snail, (100, 100))

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

    screen.blit(snail, (xvalues[0], yvalues[0]))
    screen.blit(eel, (xvalues[1], yvalues[1]))
    screen.blit(goldfish, (xvalues[2], yvalues[2]))
    screen.blit(clownfish, (xvalues[3], yvalues[3]))
    screen.blit(starfish, (xvalues[4], yvalues[4]))

    pygame.display.flip()
    screen.fill((0, 0, 0))
