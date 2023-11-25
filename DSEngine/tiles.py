import pygame
from pygame import Vector2
import DSEngine.etypes as etypes
from .saving import *

class Tile(etypes.Type2D):
    def __init__(self, parent, layer=10, position=Vector2(0, 0), texture=""):
        self.parent = parent
        self.filename = texture
        self.layer = layer
        super().__init__(layer, position, 0)
        self.text_pos = Vector2((self.position.x*self.parent.tile_size.x), (self.position.y*self.parent.tile_size.y))
        self.texture = etypes.Image2D(texture, parent.layer, position=self.text_pos)
        self.rect = self.texture.rect
    
    def render(self, window: etypes.Window):
        self.texture.window = window
        self.texture.render(window)
        super().render(window)
    
    def save_tile(self):
        data = {}
        data["filename"] = self.filename
        data["position"] = [self.position.x, self.position.y]
        data["raw_pos"] = [self.text_pos.x, self.text_pos.y]
        data["layer"] = self.layer
        return data

class TileMap(etypes.Type2D):
    def __init__(self, layer=10, position=Vector2(0.0, 0.0), tile_size=Vector2(32, 32), rotation=0):
        self.collision = True
        self.area = False
        self.tile_size = tile_size
        self.tiles = []
        super().__init__(layer, position, rotation)
    
    def collisions(self, rect2):
        for i in self.tiles:
            rect2.detect_collision(i.texture)
    
    def import_tilemap(self, filename="tilemap.sav"):
        data = load(filename)
        for i in data:
            pos = Vector2(i["position"][0], i["position"][1])
            tile = Tile(self, i["layer"], pos, i["filename"])
            self.tiles.append(tile)
            #print(tile)
        #print(data)
    
    def save_tilemap(self, filename="tilemap.sav"):
        data = []
        for i in self.tiles:
            tile_data = i.save_tile()
            data.append(tile_data)
        save(filename, data)
        #print(data)
    
    def add_tile(self, layer=0, tile_texture="", position=Vector2(0, 0)):
        tile = Tile(self, layer, position, tile_texture)
        self.tiles.append(tile)
    
    def render(self, window: etypes.Window):
        for tile in self.tiles:
            tile.render(window)
        super().render(window)
