# https://www.pygame.org/docs/ref/color.html
import math
import time
import random
import os
import pygame
from pygame.locals import *

pygame.init()

# region colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

colorList = []
colorList.append(black)
colorList.append((102, 153, 255))
colorList.append((48, 26, 75))
colorList.append((19, 154, 67))
colorList.append((11, 93, 30))
colorList.append((243, 167, 18))
colorList.append((247, 92, 3))
colorList.append("#97EFE9")
colorList.append("#CC2936")
colorList.append("#577399")
colorList.append("0x931F1D")
colorList.append("0x1A1B41")
colorList.append("0xFF9B42")
colorList.append("0xFFF275")
# endregion

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Title')
pygame.mouse.set_visible(0)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(black)
clock = pygame.time.Clock()

# pygame object for color representations
#   Color(r, g, b) -> Color
#   Color(r, g, b, a=255) -> Color
#   Color(color_value) -> Color
#       color_value supports the following formats:
#           - Color object: clones the given Color object
#           - color name str: name of the color to use, e.g. 'red'
#               https://github.com/pygame/pygame/blob/main/src_py/colordict.py
#           - HTML color format str: '#rrggbbaa' or '#rrggbb', where rr, gg, bb, and aa are 2-digit
#             hex numbers in the range of 0 to 0xFF inclusive, the aa (alpha) value defaults to 0xFF if not provided
#           - hex number str: '0xrrggbbaa' or '0xrrggbb', where rr, gg, bb, and aa are 2-digit hex numbers
#             in the range of 0x00 to 0xFF inclusive, the aa (alpha) value defaults to 0xFF if not provided
#           - int: int value of the color to use, using hex numbers can make this parameter more readable,
#             e.g. 0xrrggbbaa, where rr, gg, bb, and aa are 2-digit hex numbers in the range of 0x00 to 0xFF inclusive, note that the aa (alpha) value is not optional for the int format and must be provided
#           - tuple/list of int color values: (R, G, B, A) or (R, G, B), where R, G, B, and A are int
#             values in the range of 0 to 255 inclusive, the A (alpha) value defaults to 255 if not provided
# The Color class represents RGBA color values using a value range of 0 to 255 inclusive

index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                pygame.draw.rect(screen, colorList[index], (0, 0, 800, 600))
                index += 1
                if index < 0 or index > 12:
                    index = 0

    pygame.display.update()
    clock.tick(60)
