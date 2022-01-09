import pygame
import random
import pgzrun

from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 600
HEIGHT = 400
X0 = WIDTH // 2
Y0 = HEIGHT // 2

position = Vector2(X0,Y0)
speed = Vector2(2,2)
a = Vector2(0,2)
def update():
    global position
    global speed
    global a
    #speed += a
    position += speed
    speed += a
    if position.x <= 0 or position.x >= WIDTH:
        speed.x *= -1
    if position.y <= 0 or position.y >= HEIGHT:
        speed.y *= -1


def draw():
    screen.fill((0,0,0))
    screen.draw.circle(pos=position,radius=10,color=(0,255,255))

pgzrun.go()