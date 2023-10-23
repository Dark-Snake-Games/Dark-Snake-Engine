import pygame
from DSEngine.etypes import Rect2D, Window
from pygame.locals import *
pygame.font.init()

class Button(Rect2D):
    def __init__(self, text: str, layer=1, position=pygame.Vector2(0.0, 0.0), font = pygame.font.SysFont('Open Sans', 40)):#, size=pygame.Vector2(0.0, 0.0)):
        self.debug = False
        self.layer = layer
        self.position = position
        self.pressed = False
        self.hovered = False
        #self.rect = pygame.Rect(position.x, position.y, position.x+size.x, position.x+size.y)
        self.text = text
        self.font = font
        self.text_surface = self.font.render(self.text, False, (255, 255, 255))
        self.color_rect = self.text_surface.get_rect()
        #self.rect = self.text_surface.get_rect()
        super().__init__(layer=self.layer, position=self.position)
        #print("Initialized super()")
    
    def render(self, window: Window):
        if self.color_rect.collidepoint(window.get_mouse_pos()):
            self.hovered = True
            leftclick, _, _ = pygame.mouse.get_pressed()
            if leftclick:
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.hovered = False
        pygame.draw.rect(window.surface, (0, 0, 0), self.color_rect)
        window.surface.blit(self.text_surface, (self.position.x, self.position.y))
        #print("Sprite2D render done")

class DialougeBox(Rect2D):
    def __init__(self, character_name: str, text: str, layer=1, position=pygame.Vector2(0.0, 0.0), font_name = pygame.font.SysFont('Open Sans', 35), font_text = pygame.font.SysFont('Impact', 25)):#, size=pygame.Vector2(0.0, 0.0)):
        self.debug = False
        self.layer = layer
        self.position = position
        self.pressed = False
        self.hovered = False
        #self.rect = pygame.Rect(position.x, position.y, position.x+size.x, position.x+size.y)
        self.charname = character_name
        self.text = text
        self.font_name = font_name
        self.font_text = font_text
        self.text_surface = self.font_name.render(self.text, False, (255, 255, 255))
        self.char_text_surface = self.font_text.render(self.charname, False, (255, 255, 255))
        self.color_rect = pygame.Rect(position.x, position.y, position.z, position.y)
        #self.rect = self.text_surface.get_rect()
        super().__init__(layer=self.layer, position=self.position)
        #print("Initialized super()")
    
    def render(self, window: Window):
        sx, sy = window.size
        self.color_rect = pygame.Rect(self.position.x, self.position.y, self.position.x+sx, self.position.y+(sy-self.position.x))
        if self.color_rect.collidepoint(window.get_mouse_pos()):
            self.hovered = True
            leftclick, _, _ = pygame.mouse.get_pressed()
            if leftclick:
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.hovered = False
        pygame.draw.rect(window.surface, (0, 0, 0), self.color_rect)
        window.surface.blit(self.text_surface, (self.position.x, self.position.y))
        window.surface.blit(self.char_text_surface, (self.position.x, self.position.y))
        #print("Sprite2D render done")