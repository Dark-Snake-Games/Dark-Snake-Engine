from DSEngine import *
from pygame import Vector2
from pygame.display import update

window = Window(fps=120, size=(1280, 720))
tilemap = TileMap(2, position=Vector2(0, 0), tile_size=Vector2(32, 32), rotation=0)
tile = Tile(tilemap, texture="Test.png")
tilemap.init(window)
tile_x = 0
tile_y = 0
while window.running:
    if tile_y <= 10:
        tilemap.add_tile("Test.png", Vector2(tile_x, tile_y))
        if tile_x >= 10:
            tile_x = 0
            tile_y += 1
        else:
            tile_x += 1
    keys = window.frame()