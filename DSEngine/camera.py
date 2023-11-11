import pygame

class Camera2D:
    def __init__(self, position: pygame.Vector2) -> None:
        self.position = position
    
    def init(self, window):
        self.window = window