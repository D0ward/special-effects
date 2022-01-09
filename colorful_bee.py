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
num = 100 # количество пчёл
class Particle:
    def __init__(self, position:Vector2, color, speed:Vector2,a):
        self.position = Vector2(position.x, position.y)
        self.color = color
        self.speed = speed
        self.a = a
    def update(self):
        mouse_vec = Vector2(pygame.mouse.get_pos())
        self.a = mouse_vec - self.position
        self.a.normalize_ip()
        self.a = self.a / 5
        self.speed += self.a
        self.position += self.speed
    def draw(self):
        mouse_vec = Vector2(pygame.mouse.get_pos())
        target_vec = (mouse_vec - self.position)
        target_vec.normalize_ip()
        target_vec *= 5
        screen.draw.line(self.position, self.position + target_vec, color=(255, 255, 255))
        screen.draw.circle(pos=self.position, radius=10, color=self.color)

particles = []
for i in range(num):
    p = Particle(
        position=Vector2(random() * WIDTH, random() * HEIGHT),
        color=(255*random(), 255 *random(), 255 *random()),
        speed=Vector2(random()/1, random()/1),
        a=Vector2(random(),random())
    )
    particles.append(p)
def update():
    for p in particles:
        p.update()
def draw():
    screen.fill((0, 0, 0))
    for p in particles:
        p.draw()
pgzrun.go()