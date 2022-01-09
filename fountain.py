import pygame
import random
import pgzrun
from random import random
from random import randint
from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 600
X0 = WIDTH // 2
Y0 = HEIGHT // 2
num = 10 # количество шариков
on_pause = False
draw_debug = False


class Particle:
    def __init__(self, position:Vector2, speed, top_speed_limit, mass):
        self.position = Vector2(position.x, position.y)
        self.speed = speed
        self.start_speed = speed

        self.top_speed_limit = top_speed_limit
        self.mass = mass
        self.life = 255
    def is_alive(self):
        return self.life > 2
    def apply_force(self, force):

        self.speed += force / self.mass
    def update(self):
        if not self.is_alive():
            return
        if self.speed.length() > self.top_speed_limit:
            self.speed.scale_to_length(self.top_speed_limit)

        self.life -= 1
        self.position += self.speed
        if self.position.x < 0:
            self.position.x = WIDTH
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = HEIGHT
        if self.position.y > HEIGHT:
            self.position.y = 0

    def draw(self):
        global draw_debug
        mouse_vec = Vector2(pygame.mouse.get_pos())
        screen.draw.filled_circle(pos=self.position, radius=self.mass, color=(0, 0, self.life))

def mouse ():
    pass
particles=[]
to_delete = []
def update():
    global on_pause , to_delete , particles
    if on_pause:
        return
    gravity = Vector2(0, 0.1)

    for i in range(num):
        p = Particle(
            position=Vector2(pygame.mouse.get_pos()),
            speed=Vector2(random()*randint(-1, 1), random()*randint(-1, 1)),

            top_speed_limit=10,
            mass=10
        )
        particles.append(p)
    alive_particals = []
    for p in particles:
        p.apply_force(gravity)
        if p.is_alive():
            p.update()
            alive_particals.append(p)
        particles = alive_particals

def draw():
    screen.fill((0,0,0,))
    for p in particles:
        p.draw()

pgzrun.go()