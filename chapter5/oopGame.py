import pygame
import pymunk
import pymunk.pygame_util
from pygame.locals import *
import sys
import random

space = pymunk.Space()
space.gravity = 0, -900


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'shape.png')

            self.screen.fill((220, 220, 220))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)

        pygame.quit()
class Box:
    def __init__(self, p0=(10, 10), p1=(690, 230), d=2):
        x0, y0 = p0
        x1, y1 = p1
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)
game = App()
game.run()