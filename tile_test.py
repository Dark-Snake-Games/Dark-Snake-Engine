from DSEngine import *
from pygame import Vector2
from pygame.display import update
from os.path import exists

window = Window(fps=120, size=(1280, 720))
tilemap = TileMap(2, position=Vector2(0, 0), tile_size=Vector2(32, 32), rotation=0)
tile = Tile(tilemap, texture="Test.png")
tilemap.init(window)
tile_x = 0
tile_y = 0
saved = False
imported = False
while window.running:
    if exists("tilemap.sav"):
        #print("Exists")
        if not imported:
            tilemap.import_tilemap()
            imported = True
    else:
        if tile_y <= 10:
            tilemap.add_tile(1, "Test.png", Vector2(tile_x, tile_y))
            if tile_x >= 10:
                tile_x = 0
                tile_y += 1
            else:
                tile_x += 1
        else:
            if not saved:
                #d = tile.save_tile()
                #print(d)
                tilemap.save_tilemap()
                saved = True
    keys = window.frame()