import pygame
from pygame import Vector2
from .etypes import Type2D, Window, Image2D

class Tile(Type2D):
    def __init__(self, parent, position=Vector2(0, 0), texture=""):
        self.parent = parent
        super().__init__(parent.layer, position, 0)
        self.text_pos = Vector2((self.position.x*self.parent.tile_size.x), (self.position.y*self.parent.tile_size.y))
        self.texture = Image2D(texture, parent.layer, position=self.text_pos)
    
    def render(self, window: Window):
        self.texture.render(window)
        super().render(window)

class TileMap(Type2D):
    def __init__(self, layer=1, position=Vector2(0.0, 0.0), tile_size=Vector2(32, 32), rotation=0):
        self.tile_size = tile_size
        self.tiles = []
        super().__init__(layer, position, rotation)
    
    def add_tile(self, tile_texture="", position=Vector2(0, 0)):
        tile = Tile(self, position, tile_texture)
        self.tiles.append(tile)
    
    def render(self, window: Window):
        for tile in self.tiles:
            tile.render(window)
        super().render(window)