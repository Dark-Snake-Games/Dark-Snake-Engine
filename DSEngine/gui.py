import pygame
from DSEngine.etypes import Rect2D, Window
from pygame.locals import *
pygame.font.init()

class Button(Rect2D):
    def __init__(self, text: str, layer=1, position=pygame.Vector2(0.0, 0.0)):#, size=pygame.Vector2(0.0, 0.0)):
        self.debug = False
        self.layer = layer
        self.position = position
        #self.rect = pygame.Rect(position.x, position.y, position.x+size.x, position.x+size.y)
        self.text = text
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.font.render(self.text, False, (255, 255, 255))
        self.color_rect = self.text_surface.get_rect()
        #self.rect = self.text_surface.get_rect()
        super().__init__(layer=self.layer, position=self.position)
        #print("Initialized super()")
    
    def render(self, window: Window):
        #super().render(window)
        pygame.draw.rect(window.surface, (0, 0, 0), self.color_rect)
        window.surface.blit(self.text_surface, (self.position.x, self.position.y))
        #print("Sprite2D render done")