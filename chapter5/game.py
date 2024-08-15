# 1 - Import packages
import pygame
import pymunk
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
red = 255
green = 255
blue = 255
rng = 4
rad = 18
color = [red, green, blue]
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
BALL_WIDTH_HEIGHT = rad*2
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
FRAMES_PER_SECOND = 100
N_PIXELS_PER_FRAME = 1.5


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
space = pymunk.Space()
space.gravity = 0, -1000
clock = pygame.time.Clock()

body = pymunk.Body()
body.position = (50,350)
shape = pymunk.Circle(body,rad)
shape.density = 1
shape.elasticity = 1
space.add(body,shape)

segment_body = pymunk.Body(body_type = pymunk.Body.STATIC)
segment_shape = pymunk.Segment(segment_body, (0,20), (400,20), 5)
segment_shape.elasticity = 0.5
space.add(segment_body,segment_shape)

class createShape:
    def __init__(self, p0=(10, 10), p1=(690, 230), d=2):
        x0, y0 = p0
        x1, y1 = p1
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)
createShape()
def convert_coord(point):
    global WINDOW_HEIGHT
    return point[0], WINDOW_HEIGHT - point[1]
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
# ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

def setcolor(rng,r,g,b):
    new_red = random.randrange(-rng, rng)
    new_green = random.randrange(-rng, rng)
    new_blue = random.randrange(-rng, rng)
    r = (r + new_red)%255
    g = (g + new_green)%255
    b = (b + new_blue)%255
    return r,g,b


while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            #  mouseX, mouseY = event.pos   #  Could do this if we needed it
            ballRect = pygame.Rect(ballX-rad, ballY-rad, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
            if ballRect.collidepoint(event.pos):
                body.position = (random.randrange(MAX_WIDTH), random.randrange(MAX_HEIGHT))
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    ballX, ballY = convert_coord(body.position)
    color = setcolor(rng,color[0],color[1],color[2])
    window.fill((0,0,0))
    pygame.draw.circle(window, color,(int(ballX), int(ballY)),rad,width=6)
    pygame.draw.line(window,(255,255,255),convert_coord((0,20)),convert_coord((400,20)), 9)

    # 10 - Draw all window elements
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    space.step(1/FRAMES_PER_SECOND)
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait