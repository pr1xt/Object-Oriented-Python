import pygame
import pymunk
import pymunk.pygame_util
import math
from pygame.locals import *
import sys
import random

space = pymunk.Space()
space.gravity = 0, 1
def generate_polygon_vertices(sides, radius=120, center=(200, 200)):
    angle = 2 * math.pi / sides
    vertices = []

    for i in range(sides):
        x = center[0] + radius * math.cos(i * angle)
        y = center[1] + radius * math.sin(i * angle)
        vertices.append((round(x, 2), round(y, 2)))

    return vertices
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

            self.screen.fill((0, 0, 0))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)

        pygame.quit()
class Box:
    def __init__(self, d=2):
        sides = 6
        pts = generate_polygon_vertices(sides)
        print(pts)
        for i in range(len(pts)):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%sides], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)
if __name__ == '__main__':
    Box()

    body = pymunk.Body(mass=1, moment=10)
    body.position = (200, 100)
    # body.apply_impulse_at_local_point((0, 10))

    circle = pymunk.Circle(body, radius=20)
    circle.elasticity = 0.95
    circle.friction = 1
    space.add(body, circle)

    App().run()