# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
red = 255
green = 255
blue = 255
rad = 14
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BALL_WIDTH_HEIGHT = rad*2
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
rng = 4

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            #  mouseX, mouseY = event.pos   #  Could do this if we needed it
            # Check if the click was in the rect of the ball
            # If so, choose a random new location

            ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed  # reverse X direction

    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction

        # Update the ball's location, using the speed in two directions
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    new_red = random.randrange(-rng,rng)
    new_green = random.randrange(-rng,rng)
    new_blue = random.randrange(-rng,rng)

    red = (red + new_red)%255
    green = (green + new_green)%255
    blue = (blue + new_blue)%255

    color = [red,green,blue]
    window.fill((0,0,0))
    pygame.draw.circle(window, color,(ballX+rad, ballY+rad),rad,width=5)

    # 10 - Draw all window elements
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait