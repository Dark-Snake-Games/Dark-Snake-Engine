from DSEngine import *
from pygame import Vector2
from pygame.display import update

window = Window(fps=120, size=(1280, 720), bg=(255, 255, 255))
button = Button(text="Press me!", position=Vector2(0, 0), size=Vector2(500, 100))
button.init(window)
while window.running:
    keys = window.frame()