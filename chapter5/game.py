# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
red = 255
green = 255
blue = 255
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
FRAMES_PER_SECOND = 30
rng = 4

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 8 - Do any "per frame" actions
    new_red = random.randrange(-rng,rng)
    new_green = random.randrange(-rng,rng)
    new_blue = random.randrange(-rng,rng)

    red = (red + new_red)%255
    green = (green + new_green)%255
    blue = (blue + new_blue)%255

    color = [red,green,blue]

    window.fill(color)

    # 10 - Draw all window elements

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait