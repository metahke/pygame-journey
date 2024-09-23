import pgzrun
from pgzero.builtins import Actor, mouse, Rect
from pgzero.screen import Screen
screen: Screen

character = Actor('down')

def update():
    screen.fill('black')
    character.x += 1

def draw():
    character.draw()

pgzrun.go()
