from DSEngine import *
from pygame import Vector2
from pygame.display import update

window = Window(fps=120, size=(1280, 720))
image1 = Image2D(filename="Test.png", position=Vector2(150, 55))
image2 = Image2D(filename="Test1.png", position=Vector2(150, 55))
spritesheet1 = Spritesheet(image1, image1, image1, image1, image1, image2, image2, image2, image2, image2)
spritesheet2 = Spritesheet(image2, image1)
animationsheet = AnimationSheet(default=image1, normal=spritesheet1, back=spritesheet2)
animationsheet.save_asheet("anim.sav")
animationsheet.load_asheet("anim.sav")
while window.running:
    keys = window.frame()