import pygame
import random
import pgzrun

from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 600
HEIGHT = 400
X0 = WIDTH // 2
Y0 = HEIGHT // 2
num = 1002 # количество капель

position = [Vector2(random.random()*100, 0)]*num
a = [Vector2(0,2)]*num
speed = [Vector2(0,1)]*num
colors = [50,50,255,255]*num

for i in range(num):
    position[i] = Vector2(random.random()*1000,random.randint(0,HEIGHT))
for i in range(0,num,3):
    colors[i] = [50,50,255,255]
    colors[i+1] = [50, 50, 170, 155]
    colors[i+2] = [50, 50, 100, 100]
    speed[i] = [0,3]
    speed[i+1] = [0,2]
    speed[i+2] = [0,2]
def update():
    global position
    global speed
    global num
    for i in range(num):
        position[i] += speed[i]
        if position[i].y >= HEIGHT:
            position[i].y = 0
def draw():
    global position
    global num
    screen.fill((0,0,0))
    for i in range(num-3):
        screen.draw.filled_rect(
            Rect(position[i].x, position[i].y, 2, 7),
            pygame.color.Color(colors[i])

        )
pgzrun.go()