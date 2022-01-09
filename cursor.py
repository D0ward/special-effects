import pygame
import random
import pgzrun

from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 600
X0 = WIDTH // 2
Y0 = HEIGHT // 2
num = 10
position = [Vector2(X0,Y0)]*num
speed = [Vector2(2,2)]*num
a = [Vector2(0,1)]*num

for i in range(10):
    position[i]=Vector2(random.random()*WIDTH,random.random()*HEIGHT)
    speed[i]=Vector2(2,2)
    a[i]=(Vector2(0,1))

def update():
    global position
    global speed
    global a
    global num
    for i in range(num):
        mouse_vec = Vector2(pygame.mouse.get_pos())
        a[i] =  (mouse_vec - position[i]) *0.001
        speed[i] +=a[i]
        position[i] += speed[i]
        if position[i].x < 0 or position[i].x > WIDTH:
            speed[i].x *= -1
        if position[i].y < 0 or position[i].y > HEIGHT:
            speed[i].y *= -1

def draw():
    global num
    screen.fill((0,0,0))
    for i in range(num):
        screen.draw.circle(pos=position[i],radius=10,color=(255,255,255))


pgzrun.go()