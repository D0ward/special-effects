import pygame
import random
import pgzrun

from pgzero.rect import Rect
from pygame.math import Vector2

WIDTH = 1000
HEIGHT = 500
X0 = WIDTH // 2
Y0 = HEIGHT // 2

position = Vector2(X0,Y0)
speed = Vector2(random.random(),random.random())

def update():
    global position
    global speed
    position += speed
    rand = random.randint(-1, 1)
    speed = Vector2(random.random()*rand,random.random()*rand)


def draw():

    #screen.draw.text("pos:"+str(position),(0,0))
    #screen.draw.text(f"speed:{speed}",(0,20))
    screen.draw.circle(pos=position,radius=1,color=(0,255,255))

pgzrun.go()