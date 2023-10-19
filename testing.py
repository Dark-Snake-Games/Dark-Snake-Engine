from DSEngine import *
from pygame import Vector2, Vector3
from pygame.display import update

window = Window(size=(1280, 720))
type2d = Type2D("GUI")
rect = Rect2D(position=Vector2(150, 55), size=Vector2(5, 5))
image = Image2D(filename="Test.png", position=Vector2(150, 55))
music = AudioPlayer("beep.mp3")
type2d.init(window)
rect.init(window)
image.init(window)
while window.running:
    if not pygame.mixer.music.get_busy():
        music.play()
    keys = window.frame()
    acc = Vector2(0.0, 0.0)
    acc.x = keys[key_to_scancode("d")]-keys[key_to_scancode("a")]
    acc.y = keys[key_to_scancode("s")]-keys[key_to_scancode("w")]
    image.move(acc)