import pygame
import random
import pgzrun

from pgzero.rect import Rect

WIDTH = 1000
HEIGHT = 500
X0 = WIDTH // 2
Y0 = HEIGHT // 2

a = 10
def update():
    pass

def draw():
    screen.fill((0,0,0))
    global a
    a = 10
    screen.draw.text(f"БЕЛЫЙ ШУМ",(X0-150,Y0),fontsize=60)
    for i in range(100):
        a += 1
        screen.draw.filled_rect(
            Rect(random.random() * WIDTH  ,random.random() * HEIGHT ,3,3),
            pygame.color.Color(255,255,255)
        )
        screen.draw.filled_rect(
            Rect(random.random() * WIDTH, random.random() * HEIGHT, 2, 2),
            pygame.color.Color(100, 100, 100)
        )
        screen.draw.filled_rect(
            Rect(random.random() * WIDTH, random.random() * HEIGHT, 2, 2),
            pygame.color.Color(5, 5, 5)
        )

pgzrun.go()