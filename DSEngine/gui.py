import pygame
from DSEngine.etypes import Image2D,Rect2D, Window, key_to_scancode
from pygame.locals import *
pygame.font.init()

class Text2D(Rect2D):
    def __init__(self, text: str, layer="GUI",color=(255,255,255), position=pygame.Vector2(0.0, 0.0), font=pygame.font.SysFont('freesans', 40)):#, size=pygame.Vector2(0.0, 0.0)):
        self.debug = False
        self.layer = layer
        self.position = position
        self.text = text
        self.font = font
        self.color=color
        self.text_surface = self.font.render(self.text, False, color)
        self.color_rect = self.text_surface.get_rect()
        self.color_rect.topleft = (position.x-(self.color_rect.size[0]/2), position.y-(self.color_rect.size[1]/2))
        #self.rect = self.text_surface.get_rect()
        super().__init__(layer=self.layer, position=self.position)
        self.size=pygame.Vector2(self.color_rect.size)
        #print("Initialized super()")
    
    def render(self, window: Window):
        if self.debug:
            pygame.draw.rect(window.surface, (0, 0, 0), self.color_rect)
        if self.visible:
            window.surface.blit(self.text_surface, (self.position.x, self.position.y))
        #print("Sprite2D render done")
    def update(self):
        self.text_surface=self.font.render(self.text, False, self.color)

class Button(Rect2D):
    def __init__(self, text: str,image="", layer="GUI", position=pygame.Vector2(0.0, 0.0), font = pygame.font.SysFont('freesans', 40),size=pygame.Vector2(0,0),color=(0,0,0)):#, size=pygame.Vector2(0.0, 0.0)):
        self.debug = False
        self.layer = layer
        self.position = position
        self.pressed = False
        self.hovered = False
        self.imagesurface=None
        if image!="":
            self.imagesurface=Image2D(image)
            self.imagesurface.position=self.position
        #self.rect = pygame.Rect(position.x, position.y, position.x+size.x, position.x+size.y)
        self.text = text
        self.font = font
        
        self.text_surface = self.font.render(self.text, False, (255, 255, 255))
        if self.imagesurface!=None:
            if self.text_surface.get_rect()>self.imagesurface.rect:
                self.color_rect = self.text_surface.get_rect()
            else:
                self.color_rect=self.imagesurface.rect
        else:
            self.color_rect = self.text_surface.get_rect()
        self.color_rect.topleft = (position.x ,position.y)
        if size!=pygame.Vector2(0,0):
            self.color_rect.size=size
        #self.rect = self.text_surface.get_rect()
        super().__init__(layer=self.layer, position=self.position,color=color)
        #print("Initialized super()")
    
    def render(self, window: Window):
        self.color_rect.topleft=self.position
        if self.color_rect.collidepoint(window.get_mouse_pos()):
            self.hovered = True
        else:
            self.hovered = False
        leftclick, _, _ = pygame.mouse.get_pressed()
        if leftclick and self.color_rect.collidepoint(window.get_mouse_pos()):
            self.pressed = True
        else:
            self.pressed = False
        if self.visible:
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)
            
            if self.imagesurface!=None:
                self.imagesurface.render(window)
            else:
                pygame.draw.rect(window.surface, self.color, self.color_rect)
            
            window.surface.blit(self.text_surface, (self.position.x, self.position.y))
    def init(self,window):
        super().init(window)
        if self.imagesurface!=None:
            self.imagesurface.init(window)
        #print("Sprite2D render done")

class DialougeBox(Rect2D):
    def __init__(self, character_name: str, text: str, layer=1, position=pygame.Vector2(0.0, 0.0), font_name = pygame.font.SysFont('freesans', 35), font_text = pygame.font.SysFont('Impact', 25)):#, size=pygame.Vector2(0.0, 0.0)):
        self.debug = False
        self.layer = layer
        self.position = position
        self.pressed = False
        self.hovered = False
        # self.button = Button("Continue", position=pygame.Vector2(self.position.x, self.position.y))
        # self.button_init = False
        self.charname = character_name
        self.text = text
        self.font_name = font_name
        self.font_text = font_text
        self.text_surface = self.font_name.render(self.text, False, (255, 255, 255))
        self.char_text_surface = self.font_text.render(self.charname, False, (255, 255, 255))
        self.color_rect = pygame.Rect(position.x, position.y, position.x, position.y)
        #self.rect = self.text_surface.get_rect()
        super().__init__(layer=self.layer, position=self.position)
        #print("Initialized super()")
    
    def render(self, window: Window):
        if self.visible:
            if window.pressed_keys[13]: #or self.button.pressed:
                self.remove(window)
                # self.button.remove(window)
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)
            sx, sy = window.size
            #self.button.position = pygame.Vector2(sx, (self.position.y+(sy-self.position.y))-20)
            self.color_rect = pygame.Rect(self.position.x, self.position.y, sx, self.position.y+(sy-self.position.x))
            pygame.draw.rect(window.surface, (0, 0, 0), self.color_rect)
            window.surface.blit(self.text_surface, (self.position.x, self.position.y+50))
            window.surface.blit(self.char_text_surface, (self.position.x, self.position.y))
            #print("Sprite2D render done")