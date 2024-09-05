import pygame
import pymunk
import pymunk.pygame_util
import math
import random

space = pymunk.Space()
space.gravity = 0, 1

list_of_shapes = []
main_color = (10, 40, 50,210)
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

    def bounceOnBumpers(space, arbiter, dummy):
        shapes = arbiter.shapes
        shapes[0].color = (0, 255, 0, 255)
        shapes[1].color = (0, 255, 0, 255)
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.005)

        pygame.quit()
class Box:
    def __init__(self, d=1,sides = 4):
        global list_of_shapes
        global main_color
        pts = generate_polygon_vertices(sides)
        print(pts)
        if len(list_of_shapes) > 1:
            for i in range(len(list_of_shapes)):
                space.remove(list_of_shapes[i])
            list_of_shapes = []


        for i in range(len(pts)):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%sides], d)
            segment.elasticity = 1
            segment.friction = 1
            list_of_shapes.append(segment)
            space.add(segment)
        print(list_of_shapes)

if __name__ == '__main__':
    Box()

    body = pymunk.Body(mass=1, moment=5)
    body.position = (200 + random.randint(-30,30), 150)
    # body.apply_impulse_at_local_point((0, 10))

    sides = 4
    def call_begin(arbiter,space,data):
        return True
    def call_separate(arbiter,space, data):
        print("separate")
        global sides
        space.remove()
        sides += 1
        Box(sides=sides)

        return True
    def call_post(arbiter,space, data):
        return True


    handler = space.add_collision_handler(0,0)
    handler.begin = call_begin
    handler.separate = call_separate
    handler.post_solve = call_post

    circle = pymunk.Circle(body, radius=10)
    circle.color = main_color
    main_circle = circle
    circle.elasticity = 0.95
    circle.friction = 1
    space.add(body, circle)
    App().run()