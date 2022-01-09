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
num = 20 #количество мячей

class Particle:
    def __init__(self, position:Vector2, color, speed:Vector2,accelerate:Vector2):
        self.position = position
        self.color = color
        self.speed = speed
        self.accelerate = accelerate
    def update(self):
        self.position += self.speed
        self.speed += self.accelerate
        if self.position.y >= HEIGHT or self.position.y <= 0:
            self.speed.y *= -1
        if self.position.x >= WIDTH or self.position.x <= 0:
            self.speed.x *= -1
    def draw(self):

        # отладка
        #screen.draw.text("pos:" + str(self.position // 1) + ';' + "speed:" + str(self.speed), self.position)

        screen.draw.circle(pos=self.position, radius=10, color=self.color)

particles = [
    Particle(
        position=Vector2(random() * WIDTH, random() * HEIGHT),
        color=(255 * random(), 255 * random(), 255 * random()),
        speed=Vector2(random(), random()),
        accelerate=Vector2(random(), random())
    )for _ in range(num)
]


def update():
    for p in particles:
        p.update()

def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()
pgzrun.go()