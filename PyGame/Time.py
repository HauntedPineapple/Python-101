# https://www.pygame.org/docs/ref/time.html
import math, time, random, os
import pygame
from pygame.locals import *

pygame.init()

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Title')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == pygame.KEYUP:
            pass
        
    pygame.display.update()
    clock.tick(60)
    # pygame.time.Clock.tick updates the clock
    # tick(framerate=0) -> milliseconds
    # should be called once per frame
    # computes how many milliseconds have passed since the previous call
    # the optional framerate argument will set the maximum framerate