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
num = 12

position = [Vector2(random()*WIDTH, random()*HEIGHT)]*num
speed = [Vector2(random()*WIDTH, random()*HEIGHT)]*num
colors = [255,255,255]*num
for i in range(num):
    position[i] = Vector2(random()*WIDTH, random()*HEIGHT)
    speed[i] = Vector2(random(), random())
    colors[i] = (random()*255, random()*255, random()*255)


def update():
    global position, speed, num
    for i in range(num):
        position[i] += speed[i]
        if position[i].y >= HEIGHT or position[i].y <= 0:
            speed[i].y *= -1
        if position[i].x >= WIDTH or position[i].x <= 0:
            speed[i].x *= -1


def draw():
    global position
    global num , colors
    screen.fill((0,0,0))
    for i in range(num-3):
        screen.draw.text("pos:" + str(position[i]//1) +';'+"speed:"+str(speed[i]), position[i])
        screen.draw.circle(pos=position[i], radius=10, color=colors[i])

pgzrun.go()