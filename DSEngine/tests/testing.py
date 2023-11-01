from DSEngine import *
from pygame import Vector2
from pygame.display import update

window = Window(fps=120, size=(1280, 720))
type2d = Type2D("GUI")
rect = Rect2D(position=Vector2(150, 55), size=Vector2(5, 5))
image1 = Image2D(filename="Test.png", position=Vector2(150, 55))
image2 = Image2D(filename="Test1.png", position=Vector2(150, 55))
spritesheet1 = Spritesheet(image1, image1, image1, image1, image1, image2, image2, image2, image2, image2)
spritesheet2 = Spritesheet(image2, image1)
animationsheet = AnimationSheet(default=image1, normal=spritesheet1, back=spritesheet2)
sprite = AnimatedSprite2D(sheet=animationsheet, position=Vector2(150, 55))
track0 = AudioPlayer("beep.mp3")
audio_man = AudioManager(beep=track0)
type2d.init(window)
rect.init(window)
sprite.init(window)
#print(audio_man.tracks)
while window.running:
    keys = window.frame()
    print(sprite.is_colliding_with(rect))
    acc = Vector2(0.0, 0.0)
    acc.x = (keys[key_to_scancode("d")]-keys[key_to_scancode("a")])*window.delta
    acc.y = (keys[key_to_scancode("s")]-keys[key_to_scancode("w")])*window.delta
    if not pygame.mixer.music.get_busy() and not sprite.playing and acc != Vector2(0.0, 0.0):
        sprite.play_sheet("normal")
        audio_man.play("beep")
    sprite.move(acc)