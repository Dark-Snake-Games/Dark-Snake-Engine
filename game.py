from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit
from random import randint

from DSEngine.animated import AnimationSheet
from DSEngine.etypes import pygame
default_title="Project: SCP"

class SCP999(AnimatedSprite2D):
    def __init__(self, position=...):
        sheet = AnimationSheet(default=Image2D("Test.png"))
        self.last_secs = 0
        super().__init__(sheet, 1, position)
    
    def render(self, window: Window):
        if int(window.seconds-self.last_secs) >= 20:
            rx = randint(0, window.size[0])
            ry = randint(0, window.size[1])
            pos = Vector2(rx, ry)
            self.move_towards(pos)
            self.last_secs = int(window.seconds)
        super().render(window)

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
    audio_man = AudioManager()
    text = Text2D("SCP-999", position=Vector2(550, 0))
    scp = SCP999(position=Vector2(640, 360))
    text.init(window)
    scp.init(window)
    scp.move_towards(Vector2(0, 0))
    while window.running:
        keys = window.frame()
        if keys[27]:
            return 1

if __name__ == "__main__":
    main_menu()