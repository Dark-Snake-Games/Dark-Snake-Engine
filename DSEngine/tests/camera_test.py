from DSEngine import *
from pygame import Vector2

window = Window(fps=120, size=(1280, 720))
camera2d = Camera2D(position=Vector2(0, 100))
window.current_camera = camera2d
rect = Rect2D(position=Vector2(150, 55), size=Vector2(100, 100))
img = Image2D("Test.png")
rect.init(window)
img.init(window)
while window.running:
    camera2d.position.x += 1
    keys = window.frame()