import pygame
import pgzrun
import math
from random import random
from random import randint
from pgzero.rect import Rect
from pygame.math import Vector2
from pygame.surface import Surface

WIDTH = 1000
HEIGHT = 600
X0 = WIDTH // 2
Y0 = HEIGHT // 2
gravity = Vector2(0,0.2)

def random_vector():
    angle = randint(0, 360)
    return Vector2(1, 0).rotate(angle)
class Particle:
    def __init__(self, position:Vector2, speed, is_firework=False, mass=1):
        self.position = Vector2(position.x, position.y)
        self.speed = speed
        self.is_firework = is_firework
        self.mass = mass
        self.start_speed = speed
        self.life = 255
        self.a = Vector2(0, 0)
    def is_alive(self):
        return self.life > 0
    def apply_force(self, force):
        self.speed += force / self.mass
    def update(self):
        self.life -= 1
        if self.is_alive():
            self.speed += self.a
            if not self.is_firework:
                self.velocity = self.speed * 0.9
                self.life -= 4
            self.position += self.speed
            self.a = Vector2(0, 0)


    def draw(self, surface: Surface):
        global fireworks
        if self.is_alive():
            red = self.life * random()
            green = self.life * random()
            blue = self.life * random()
            if self.is_firework:
                color = (red, green, blue)
            else:
                color = (red, green, blue)
            pygame.draw.circle(surface, center=self.position, radius=2, color=color)
        else:
            return

class Firework:
    def __init__(self, pos:Vector2):
        self.firework = Particle(position=pos, speed=Vector2(0, randint(-12, -8)))
        self.is_exploaded = False
        self.particles =[]
    def update(self):
        global gravity
        if not self.is_exploaded:
            self.firework.apply_force(gravity)
            self.firework.update()
            if self.firework.velocity.y > 0 and not self.is_exploaded:
                self.is_exploaded = True
                self.explode()
        for p in self.particles:
            p.apply_force(gravity)
            p.update()
    def draw(self, surface: Surface):
        if not self.is_exploaded:
            self.firework.draw(surface)
        for p in self.particles:
            p.draw(surface)

    def explode(self):
        for i in range(50):
            velocity: Vector2 = random_vector() * randint(2, 10)
            self.particles.append(Particle(
                position=Vector2(self.firework.position),
                speed=velocity,
                is_firework=False
                )
            )
fireworks = []

def update():
    global fireworks
    for firework in fireworks:
        firework.update()
    if randint(0, 100) > 85:
        fireworks.append(Firework(pos=Vector2(randint(0, WIDTH), HEIGHT -10)))
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
def draw():
    surface.fill((0, 0, 0,25))
    for firework in fireworks:
        firework.draw(surface)
    screen.blit(surface, pos=(0, 0))


pgzrun.go()