from DSEngine import *
from pygame import Vector2
from pygame.display import update

old_pressed = False
window = Window(fps=120, size=(1280, 720), bg=(255, 255, 255))
button = Button(text="Press me!", position=Vector2(0, 0))
button.init(window)
# dialouge_text = """Why am I doing this?
# I am not even paid!"""
# dialouge0 = DialougeBox("R9_", dialouge_text, position=Vector2(0, 550))
# dialouge0.init(window)
while window.running:
    keys = window.frame()
    print(button.pressed)
#     if button.pressed != old_pressed:
#         if button.pressed:
#             print("Pressed")
#         else:
#             print("Not pressed")
#         old_pressed = button.pressed
