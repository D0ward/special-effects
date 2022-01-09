import pygame
import random
import pgzrun
from pygame import key
from random import random
from random import randint
from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 600
X0 = WIDTH // 2
Y0 = HEIGHT // 2


gravity = Vector2(0,0.2)
back_ground = [
    pygame.transform.scale(pygame.image.load('moon.jpg'), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load('mars.jpg'), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load('venera.jpg'), (WIDTH, HEIGHT)),
    pygame.transform.scale(pygame.image.load('cosmos.jpg'), (WIDTH, HEIGHT))
]

i = 0

def on_key_down(key):
    global gravity
    if key == pygame.K_w:
        gravity = Vector2(0,-0.2)
    if key == pygame.K_a:
        gravity = Vector2(-0.2, 0)
    if key == pygame.K_s:
        gravity = Vector2(0, 0.2)
    if key == pygame.K_d:
        gravity = Vector2(0.2, 0)
#f = False
last_planet = 0
class Particle:
    global last_planet
    def __init__(self, position:Vector2, color, speed:Vector2, mass):
        self.position = Vector2(position.x, position.y)
        self.color = color
        self.speed = speed
        self.mass = mass
    def update(self):
        global i , back_ground , last_planet
        self.position += self.speed
        if self.position.y >= HEIGHT:
            if i == 3:
                i = last_planet
            else:
                self.speed.y *= -1
        if self.position.x > WIDTH:
            self.position.x = 0
            if i < 2:
                i += 1
            else:
                i = 0
        if self.position.x < 0:
            self.position.x = WIDTH
            if i > 0:
                i -= 1
            else:
                i = 2
        if self.position.y < 0:
            if i == 3:
                self.speed.y *= -1
            else:
                last_planet = i
                i = 3
                self.position.y = HEIGHT
        self.apply_force(gravity)
        if pygame.key.get_focused():
            on_key_down(pygame.key.get_pressed())
        #
    def apply_force(self, force):
        self.speed += force / self.mass

    def draw(self):
        screen.draw.filled_circle(pos=self.position, radius=self.mass,color=(205,205,205))

particles = [
    Particle(
        position=Vector2(random() * WIDTH, random() * HEIGHT),
        color=(255 * random(), 255 * random(), 255 * random()),
        speed=Vector2(random(), random()),
        mass=15
    )
]

def update():
    for p in particles:
        p.update()

def draw():

    global i, back_ground
    screen.surface.blit(source=back_ground[i], dest=(0, 0))
    screen.draw.text(f"Менять направление полёта на WASD",Vector2(10,10))
    for p in particles:
        p.draw()

pgzrun.go()