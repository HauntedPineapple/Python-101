import math
import pygame

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

cornflower_blue = (102, 153, 255)
# endregion

gameDisplay = pygame.display.set_mode((600, 600))

gameDisplay.fill(black)

# https://www.pygame.org/docs/ref/draw.html?highlight=draw#module-pygame.draw

# All the drawing functions accept a color argument that can be one of the following formats:
#     - a pygame.Color pygame object for color representations object
#           - https://www.pygame.org/docs/ref/color.html
#     - an (RGB) triplet (tuple/list)
#     - an (RGBA) quadruplet (tuple/list)
#     - an integer value that has been mapped to the surface's pixel format
#           - https://www.pygame.org/docs/ref/surface.html#pygame.Surface.map_rgb
#           - https://www.pygame.org/docs/ref/surface.html#pygame.Surface.unmap_rgb
# A color's alpha value will be written directly into the surface (if the surface contains pixel alphas), but the draw function will not draw transparently
# These functions temporarily lock the surface they are operating on.
# Many sequential drawing calls can be sped up by locking and unlocking the surface object around the draw calls:
#   https://www.pygame.org/docs/ref/surface.html#pygame.Surface.lock
#   https://www.pygame.org/docs/ref/surface.html#pygame.Surface.unlock

# surface (Surface) -- surface to draw on

# Pixel
pixArr = pygame.PixelArray(gameDisplay)
pixArr[10][10] = red
pixArr[12][12] = red
# what we're doing is assigning the entire pixel array to a value, referencing it using pygame.PixelArray.
# So what this function does is it returns the pixel array of the specified surface
# (which is the entire display in our case).
# Then, we're able to modify it. So, we specify pixAr[10][20],
# which means the pixel residing at (10,20), then we're able to re-assign it.
# In our case, we call it green.

# Lines: https://www.pygame.org/docs/ref/draw.html#pygame.draw.line
# line(surface, color, start_pos, end_pos, width=1)
# start_pos (tuple(int/float, int/float) or list[int or float, int/float] or Vector2(int/float, int/float)) -- start position of the line, (x, y)
# end_pos (tuple(int/float, int/float) or list[int/float, int/float] or Vector2(int/float, int/float)) -- end position of the line, (x, y)
#       https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2
# width (int, optional) used for line thickness
pygame.draw.line(gameDisplay, green, (150, 325), (250, 450), 5)
# where do we want to draw it, what color do we want it,
# and then we specify the two coordinate pairs that we want to draw a line between

# Rectangles: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
# rect(surface, color, rect, width=0, border_radius=0, border_top_left_radius=-1,
# border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
pygame.draw.rect(gameDisplay, blue, (330, 120, 90, 50))
# where to draw, what color, and then a tuple that contains:
# the top left x and y, followed by width, then height
# Rect(left, top, width, height) -> Rect
# Rect((left, top), (width, height)) -> Rect
# width is used for line thickness or to indicate that the rectangle is to be filled
#   - if width == 0, (default) fill the rectangle
#   - if width > 0, used for line thickness
#   - if width < 0, nothing will be drawn
# When using width values > 1, the edge lines will grow outside the original boundary of the rect

# Circles: https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
# circle(surface, color, center, radius, width=0,
# draw_top_right=None, draw_top_left=None, draw_bottom_left=None, draw_bottom_right=None)
pygame.draw.circle(gameDisplay, cyan, (150, 150), 75)
# where to draw, what color, what is the center point of the circle, and what is the radius

# Polygons: https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon
# polygon(surface, color, points, width=0)
# Drawn using a tuple or list of coordinates (tuple, list, Vector2) in a sequence of 3 or more
# (x,y) coordinates in clockwise order
pygame.draw.polygon(gameDisplay, magenta, ((540, 330), (540, 420),
                    (540, 510), (510, 450), (450, 390), (510, 390)))
#

# Ellipses: https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse
# ellipse(surface, color, rect, width=0)
# rect (Rect) -- rectangle to indicate the position and dimensions of the ellipse,
# the ellipse will be centered inside the rectangle and bounded by it
pygame.draw.ellipse(gameDisplay, white, [200, 200, 210, 130], 0)

# Elliptical Arc: https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc
# arc(surface, color, rect, start_angle, stop_angle, width=1)
# Angles are in radians
# if start_angle < stop_angle, the arc is drawn in a counterclockwise direction from the start_angle to the stop_angle
# if start_angle > stop_angle, tau (tau == 2 * pi) will be added to the stop_angle,
# if the resulting stop angle value is greater than the start_angle the above start_angle < stop_angle case applies, 
# otherwise nothing will be drawn
# if start_angle == stop_angle, nothing will be drawn
pygame.draw.arc(gameDisplay, yellow, [
                450, 100, 250, 200],  math.pi/2, math.pi, 2)

# See the pygame.gfxdrawpygame module for drawing shapes module for alternative draw methods:
# https://www.pygame.org/docs/ref/gfxdraw.html#module-pygame.gfxdraw

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()