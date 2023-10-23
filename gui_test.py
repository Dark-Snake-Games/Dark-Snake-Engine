from DSEngine import *
from pygame import Vector2
from pygame.display import update

old_pressed = False
window = Window(fps=120, size=(1280, 720))
button = Button(text="Press me!", position=Vector2(0, 0))
button.init(window)
while window.running:
    keys = window.frame()
    if button.pressed != old_pressed:
        if button.pressed:
            print("Pressed")
        else:
            print("Not pressed")
        old_pressed = button.pressed