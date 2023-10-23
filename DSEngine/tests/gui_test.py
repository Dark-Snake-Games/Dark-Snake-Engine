from DSEngine import *
from pygame import Vector2
from pygame.display import update

window = Window(fps=120, size=(1280, 720))
inputbox = InputBox(position=Vector2(0, 0), size=Vector2(100, 100))
inputbox.init(window)
while window.running:
    keys = window.frame()