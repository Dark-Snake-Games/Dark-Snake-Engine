from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit
from random import randint
default_title="Project: SCP"

def main_menu():
    global default_title
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    audio_man = AudioManager()
    text = Text2D("Project: SCP", position=Vector2(530, 150))
    play_button = Button("Play", position=Vector2(595, 280))
    exit_button = Button("Exit", position=Vector2(600, 380))
    text.init(window)
    play_button.init(window)
    exit_button.init(window)
    while window.running:
        keys = window.frame()
        if keys[27]:
            #exit(1)
            pass
        elif play_button.pressed:
            scp_999_scene()
            play_button.pressed = False
        elif exit_button.pressed:
            exit(1)
        else:
            #print("Nothing pressed")
            pass

def scp_999_scene():
    global default_title
    window = Window(title=default_title, fps=120, size=(1280, 720), bg=(100, 100, 100))
    last_secs = 0
    audio_man = AudioManager()
    text = Text2D("SCP-999", position=Vector2(550, 0))
    animations = AnimationSheet(default=Image2D("Test.png"))
    scp = AnimatedSprite2D(animations, position=Vector2(640, 360))
    text.init(window)
    scp.init(window)
    scp.move_towards(Vector2(0, 0))
    while window.running:
        if int(window.seconds-last_secs) >= 10:
            rx = randint(0, window.size[0])
            ry = randint(0, window.size[1])
            pos = Vector2(rx, ry)
            scp.move_towards(pos)
            last_secs = int(window.seconds)
        keys = window.frame()
        if keys[27]:
            return 1

if __name__ == "__main__":
    main_menu()