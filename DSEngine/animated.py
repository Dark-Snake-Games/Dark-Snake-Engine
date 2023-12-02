import pygame
from DSEngine.etypes import *
from DSEngine.saving import save, load
from pygame.locals import *

class Spritesheet:
    def __init__(self, delay: int = 0, *spritesheet):
        self.sheet = []
        self.delay = 0
        for i in spritesheet:
            if type(i) == Image2D:
                #print(i.name)
                self.sheet.append(i)

class AnimationSheet:
    def __init__(self, default: Image2D, **spritesheets):
        self.sheets = spritesheets
        self.default = default
    
    def save_asheet(self, filename: str):
        data = {}
        for i in self.sheets.keys():
            d = []
            data["default"] = self.default.name
            for j in self.sheets[i].sheet:
                if type(j) == Image2D:
                    d.append(j.name)
            data[i] = d
        save(filename, data)
        #print(data)
    
    def load_asheet(self, filename: str):
        data = load(filename)
        self.default = data["default"]
        data["default"] = None
        for i in data.keys():
            d = Spritesheet()
            if data[i] != None:
                for j in data[i]:
                    img = Image2D(j)
                    d.sheet.append(img)
                self.sheets[i] = d
        #print(self.sheets)

class AnimatedSprite2D(Rect2D):
    def __init__(self, sheet: AnimationSheet, layer=1, position=pygame.Vector2(0.0, 0.0),size=None,offset=pygame.Vector2(0,0)):#, size=pygame.Vector2(0.0, 0.0)):
        self.sprite = pygame.sprite.Sprite()
        self.debug = False
        self.layer = layer
        self.position = position
        self.sprites = sheet
        self.current_sheet = self.sprites.sheets
        self.sheet_name = ""
        self.curent_frame = 0
        self.sheet_length = -1
        self.playing = False
        self.moving_towards = False
        self.collisionoffset=offset
        self.image = self.sprites.default.image
        if size==None:
            self.size = pygame.Vector2(self.image.get_width(), self.image.get_height())
        else:
            self.size=size
        self.rect = pygame.Rect(position.x+offset.x, position.y+offset.y, self.size.x, self.size.y)
        self.image = self.image.convert_alpha()
        super().__init__(layer=self.layer, position=self.position,size=self.size,offset=offset)
    
    def stop_playing(self):
        self.playing = False
        self.frame = 0

    def play_sheet(self, name: str):
        self.current_sheet = self.sprites.sheets[name]
        self.sheet_name = name
        self.frame = 0
        self.sheet_length = len(self.current_sheet.sheet)
        self.playing = True
    
    def move_towards(self, pos=pygame.Vector2()):
        self.steps = max(abs(pos.x-self.position.x), abs(pos.y-self.position.y))
        self.stepx = float(pos.x-self.position.x)/self.steps
        self.stepy = float(pos.y-self.position.y)/self.steps
        self.step = 0
        self.moving_towards = True
    
    def render(self, window: Window):
        if self.visible:
            self.detect_collisions()
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)
            if self.moving_towards:
                vel = pygame.Vector2(self.stepx, self.stepy)
                self.move(vel)
                self.step += 1
                if self.step >= self.steps: self.moving_towards = False
            if self.current_sheet != self.sprites.sheets and self.frame < self.sheet_length:
                self.image = self.current_sheet.sheet[self.frame].image
                self.frame += 1
                self.playing = True
            else:
                self.sheet_name = ""
                self.image = self.sprites.default.image
                self.current_sheet = self.sprites.sheets
                self.frame = 0
                self.sheet_length = -1
                self.playing = False
            unoffset=pygame.Vector2(self.collisionoffset.x,self.collisionoffset.y)
            window.surface.blit(self.image, self.rect.topleft-unoffset)
            if self.debug:
                pygame.draw.rect(window.surface, (255, 255, 255), self.rect)
                super().render(window)