import pygame, sys
from .camera import Camera2D
#from .tiles import TileMap

def key_to_scancode(key: str):
    return pygame.key.key_code(key)

class Window:
    def __init__(self, fps=60, title="DSEngine Window", size: tuple=(800, 600), bg: tuple=(0, 0, 0), icon=pygame.image.load("default.icon.png"), zoom=pygame.Vector2(1,1)):
        self.layers = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[],
                       7:[], 8:[], 9:[], 10:[], "GUI":[]}
        print("Window init")
        self.fps, self.title, self.size, self.bg, self.icon, self.zoom = fps, title, size, bg, icon, zoom
        self.surface = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.delta = 0
        self.elapsed_ms = 0
        self.seconds = 0
        self.current_camera = Camera2D(position=pygame.Vector2(0, 0))
        self.pressed_keys = pygame.key.get_pressed()
        self.prev_keys=pygame.key.ScancodeWrapper()
    
        pygame.display.set_icon(icon)
        pygame.display.set_caption(title)
        self.bg_rect = pygame.Rect(0, 0, size[0], size[1])
        if bg != (0, 0, 0):
            self.surface.fill(bg)
            pygame.display.flip()
        self.running = True
    
    def get_mouse_pos(self):
        x, y = pygame.mouse.get_pos()
        return pygame.Vector2(x, y)
    
    def frame(self):
        
        self.prev_keys=self.pressed_keys
        global keys
        self.delta = self.clock.tick(self.fps)
        self.elapsed_ms += self.delta
        self.seconds = self.elapsed_ms/100
        pygame.draw.rect(self.surface, self.bg, self.bg_rect)
        for event in pygame.event.get():      
            if event.type == pygame.QUIT: 
                self.running = False
                pygame.quit()
                sys.exit()
        for j in range(1, 10+1):
            #print(j)
            for i in self.layers[j]:
                i.render(self)
        for i in self.layers["GUI"]:
            i.render(self)
        if self.zoom!=pygame.Vector2(1,1):
            surface=pygame.transform.scale(self.surface,(self.size[0]*self.zoom.x, self.size[1]*self.zoom.y))
            self.surface.blit(surface,(0,0))
        pygame.display.flip()
        pygame.display.update()
        self.pressed_keys = pygame.key.get_pressed()
        return self.pressed_keys
    
    def key_just_pressed(self,scancode:int):
        return self.pressed_keys[scancode] and not self.prev_keys[scancode]
    


        

class Type2D:
    def __init__(self, layer=1, position=pygame.Vector2(0.0, 0.0), rotation=0.0):
        self.layer = layer
        self.position = position
        self.rotation = rotation
    
    def init(self, window: Window):
        window.layers[self.layer].append(self)
        self.window = window
    
    def remove(self, window: Window):
        window.layers[self.layer].remove(self)
        self.window = None
    
    def render(self, window: Window):
        pass

class Rect2D(Type2D):
    def __init__(self, layer=1, position=pygame.Vector2(0.0, 0.0), color=(255, 255, 255), size=pygame.Vector2(100.0, 100.0),offset=pygame.Vector2(0,0)):
        self.sprite = pygame.sprite.Sprite()
        self.visible=True
        self.collision=True
        self.window = None
        self.layer = layer
        self.position = position
        self.color = color
        self.size = size
        self.collisionoffset=offset
        self.area = False
        self.prev_pos = self.position
        self.rect = pygame.Rect(position.x+self.collisionoffset.x, position.y+self.collisionoffset.y, size.x, size.y)
        self.collision_sides = {"left":False, "right":False,
                                "bottom":False, "top":False}
        super().__init__(layer=self.layer, position=self.position)

    def is_on_floor(self):
      return self.collision_sides["bottom"]

    def is_on_ceiling(self):
      return self.collision_sides["top"]

    #def detect_collision(self, i):
        #if i != self and "type(i) == Rect2D" and not i.area and i.collision:
            #side = self.get_collision_side(i)
            #if side != None:
                #self.collision_sides[side] = True

    
    def detect_collisions(self):
        if self.collision and self.window != None:
            self.collision_sides = {"left":False, "right":False,
                                    "bottom":False, "top":False}
            for i in self.window.layers[self.layer]:
                if i != self and "type(i) == Rect2D" and not i.area and i.collision:
                    side = self.get_collision_side(i)
                    if side != None:
                        self.collision_sides[side] = True

                #if type(i) == TileMap:
                    #i.collisions()
                #else:
                #self.detect_colision(i)
        
    def get_collision_side(self, rect2):
        if self.is_colliding_with(rect2):
            dr = abs(self.rect.right - rect2.rect.left)
            dl = abs(self.rect.left - rect2.rect.right)
            db = abs(self.rect.bottom - rect2.rect.top)
            dt = abs(self.rect.top - rect2.rect.bottom)
            if min(dl, dr) < min(dt, db):
                direction = "left" if dl < dr else "right"
            else:
                direction = "bottom" if db < dt else "top"
            return direction
        else:
            return None
    
    def is_colliding_with(self, rect2: Type2D):
        return self.rect.colliderect(rect2.rect)
    
    def render(self, window: Window):
        if self.visible:
            self.window = window
            self.detect_collisions()
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)
            pygame.draw.rect(window.surface, self.color, self.rect)
            super().render(window)
    
    def is_moving(self):
        return self.prev_pos == self.position
    
    def move(self, vec: pygame.Vector2):
        oldpos = self.position
        oldtl = self.rect.topleft
        vecx = vec.x
        vecy = vec.y
        self.position = pygame.Vector2(self.position.x+vecx, self.position.y+vecy)
        self.rect.topleft = (self.position.x, self.position.y)
        if vecx > 0:
            if not self.collision_sides["right"]:
                pass
            else:
                self.position.x = oldpos.x
                self.rect.topleft = (oldpos.x, self.rect.topleft[1])
        else:
            if not self.collision_sides["left"]:
                vecx = vecx
            else:
                self.position.x = oldpos.x
                self.rect.topleft = (oldpos.x, self.rect.topleft[1])
        if vecy > 0:
            if not self.collision_sides["bottom"]:
                pass
            else:
                self.position.y = oldpos.y
                self.rect.topleft = (self.rect.topleft[0], oldpos.y)
        else:
            if not self.collision_sides["top"]:
                vecy = vecy
            else:
                self.position.y = oldpos.y
                self.rect.topleft = (self.rect.topleft[0], oldpos.y)
        self.rect.topleft+=self.collisionoffset
        #self.position = pygame.Vector2(self.position.x+vecx, self.position.y+vecy)
        #self.rect.topleft = (self.position.x, self.position.y)
        self.prev_pos = self.position

class Surface(Rect2D):
    def __init__(self, layer=1, position=pygame.Vector2(0.0, 0.0), color=(255, 255, 255), size=pygame.Vector2(100.0, 100.0),offset=pygame.Vector2(0,0)):
        super().__init__(layer,position,color,size,offset)
        self.surface=pygame.Surface(size)
        self.layers = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[],
                       7:[], 8:[], 9:[], 10:[], "GUI":[]}
        self.window=None
        self.elapsed_ms=0
        self.current_camera = Camera2D(position=pygame.Vector2(0, 0))
        self.pressed_keys,self.prev_keys=pygame.key.ScancodeWrapper(),pygame.key.ScancodeWrapper()
    
    def render(self, window: Window):
        if self.visible:
            self.window = window
            self.detect_collisions()
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)
            window.surface.blit(self.surface,self.position,self.rect)
    
    def frame(self):
        self.prev_keys=self.pressed_keys
        self.pressed_keys = pygame.key.get_pressed()
        if self.window !=None:
            global keys
            self.delta = self.window.clock.tick(self.window.fps)
            self.elapsed_ms += self.delta
            self.seconds = self.elapsed_ms/100
            pygame.draw.rect(self.surface, (0,0,0), self.rect)
            for event in pygame.event.get():      
                if event.type == pygame.QUIT: 
                    self.running = False
                    pygame.quit()
                    sys.exit()
            for j in range(1, 10+1):
                #print(j)
                for i in self.layers[j]:
                    i.render(self)
            for i in self.layers["GUI"]:
                i.render(self)
            self.window.frame()
            pygame.display.flip()
            pygame.display.update()
            
        
        return self.pressed_keys
    
    def key_just_pressed(self,scancode:int):
        return self.pressed_keys[scancode] and not self.prev_keys[scancode]
                

class Image2D(Rect2D):
    def __init__(self, filename: str, layer=1, position=pygame.Vector2(0.0, 0.0),offset=pygame.Vector2(0,0)):#, size=pygame.Vector2(0.0, 0.0)):
        self.sprite = pygame.sprite.Sprite()
        self.debug = False
        self.layer = layer
        self.position = position
        self.name = filename
        self.image = pygame.image.load(self.name)
        
        self.image = self.image.convert_alpha()
        super().__init__(layer=self.layer, position=self.position)
        
        self.rect = self.image.get_rect()
        self.size=pygame.Vector2(self.rect.size)
        self.collisionoffset=offset
        self.rect.x += self.collisionoffset.x
        self.rect.y += self.collisionoffset.y
    
    def render(self, window: Window):
        if self.visible:
            unoffset=pygame.Vector2(self.collisionoffset.x,self.collisionoffset.y)
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)
            window.surface.blit(self.image, self.rect.topleft-unoffset)
            self.detect_collisions()
            if self.debug:
                super().render(window)
    def changeimage(self,source,changecollision=True):
        self.image = pygame.image.load(source)
        self.name=source
        self.image = self.image.convert_alpha()
        
        if changecollision:
            self.rect = self.image.get_rect()
            self.rect.x += self.collisionoffset.x
            self.rect.y += self.collisionoffset.y

class Area2D(Rect2D):
    def __init__(self, layer: int = 1, position=pygame.Vector2(0.0, 0.0), size=pygame.Vector2(0.0, 0.0)):#, size=pygame.Vector2(0.0, 0.0)):
        self.sprite = pygame.sprite.Sprite()
        self.debug = False
        self.layer = layer
        self.position = position
        self.bodies_touching = []
        self.areas_touching = []
        self.area = True
        self.size = size
        super().__init__(layer=self.layer, position=self.position, size=size)
    
    def detect_collisions(self):
        self.bodies_touching = []
        self.areas_touching = []
        for i in self.window.layers[self.layer]:
            if i != self and type(i) == Rect2D and not i.area and i.collision:
                side = self.get_collision_side(i)
                if side != None:
                    if not i.area:
                        self.bodies_touching.append(i)
                    else:
                        self.areas_touching.append(i)
    
    def render(self, window: Window):
        if self.visible:
            self.rect.topleft = (self.position.x+self.collisionoffset.x+window.current_camera.position.x, self.position.y+self.collisionoffset.y+window.current_camera.position.y)

            # window.surface.blit(self.image, self.rect)
            self.detect_collisions()
            if self.debug:
                super().render(window)

class AudioManager:
    def __init__(self, **tracks):
        self.tracks = {}
        for i in tracks.keys():
            if type(tracks[i]) == AudioPlayer:
                self.tracks[i] = tracks[i]
    
    def play(self, track):
        try:
            self.tracks[track].play()
            return 0
        except KeyError:
            return -1

class AudioPlayer:
    def __init__(self, file: str) -> None:
        self.f = pygame.mixer.Sound(file)
        self.chan = pygame.mixer.find_channel()
        self.chan.queue(self.f)

    def play(self):
        self.chan.queue(self.f)
    
    def pause(self):
        self.chan.pause()
    
    def resume(self):
        self.chan.unpause()

