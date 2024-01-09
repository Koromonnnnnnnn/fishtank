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
