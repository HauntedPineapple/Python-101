# Source: https://www.pygame.org/docs/tut/ChimpLineByLine.html
import os
import pygame
from pygame.locals import *

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

pygame.init()
screen = pygame.display.set_mode((800, 600)) # Width, Height
pygame.display.set_caption('Title')
pygame.mouse.set_visible(0)

background = pygame.Surface(screen.get_size())
# This creates a new surface for us that is the same size as the display window
background = background.convert()
background.fill((250, 250, 250))

def load_image(filename, colorkey=None):
    '''Takes the name of an image to load and takes an optional argument it can use to set a colorkey for the image'''
    fullname = os.path.join('resources', filename)
    # Creates a full pathname to the file in the folder named 'resources'

    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', filename)
        raise SystemExit(message)

    image = image.convert()

    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    return image, image.get_rect()

def load_sound(filename):
    '''Takes the name of sound to load'''
    class NoneSound:
        def play(self): pass

    if not pygame.mixer:
        # Checks to see if module was imported successfully
        return NoneSound()

    fullname = os.path.join('resources', filename)
    # Creates a full pathname to the file in the folder named 'resources'

    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print('Cannot load sound:', fullname)
        raise SystemExit(message)

    return sound

clock = pygame.time.Clock()
display_start_menu = True
playing = False
game_over = False

def game():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    if display_start_menu == True:
        start_menu()
    elif playing == True:
        game_loop()
    elif game_over == True:
        game_over_screen()
    

def start_menu():
    for event in pygame.event.get():            
        if event.type == KEYDOWN:
            if event.key == K_KP_ENTER:
                display_start_menu == False
                playing = True

def game_loop():
    while not game_over:
        # region input handling
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

                if event.key == K_w or event.key == K_UP:
                    pass
                if event.key == K_a or event.key == K_LEFT:
                    pass
                if event.key == K_s or event.key == K_DOWN:
                    pass
                if event.key == K_d or event.key == K_RIGHT:
                    pass

            if event.type == pygame.KEYUP:
                pass
        # endregion

        pygame.display.update()
        clock.tick(60)
        # Ensures the game runs no more than 60fps

def game_over_screen():
    while game_over:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_KP_ENTER:
                    playing = True
        


game()
pygame.quit()
quit()