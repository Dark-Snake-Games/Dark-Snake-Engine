from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit

def main_menu():
    window = Window(fps=120, size=(1280, 720), bg=(100, 100, 100))
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
    window = Window(fps=120, size=(1280, 720), bg=(100, 100, 100))
    audio_man = AudioManager()
    text = Text2D("SCP-999", position=Vector2(550, 0))
    scp = Image2D("Test.png", position=Vector2(640, 360))
    text.init(window)
    scp.init(window)
    while window.running:
        keys = window.frame()
        if keys[27]:
            return 1
        else:
            pass

if __name__ == "__main__":
    main_menu()