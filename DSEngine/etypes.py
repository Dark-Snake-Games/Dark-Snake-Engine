import pygame, sys

def key_to_scancode(key: str):
    return pygame.key.key_code(key)

class Window:
    def __init__(self, fps=60, title="DSEngine Window", size: tuple=(800, 600), bg: tuple=(0, 0, 0), icon=pygame.image.load("default.icon.png")):
        self.layers = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[],
                       7:[], 8:[], 9:[], 10:[], "GUI":[]}
        print("Window init")
        self.fps, self.title, self.size, self.bg, self.icon = fps, title, size, bg, icon
        self.surface = pygame.display.set_mode(size)
        self.clock = pygame.time.Clock()
        self.delta = 0
        self.elapsed_ms = 0
        self.seconds = 0
        self.pressed_keys = pygame.key.get_pressed()
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
        pygame.display.flip()
        pygame.display.update()
        self.pressed_keys = pygame.key.get_pressed()
        return self.pressed_keys

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
    def __init__(self, layer=1, position=pygame.Vector2(0.0, 0.0), color=(255, 255, 255), size=pygame.Vector2(100.0, 100.0)):
        self.sprite = pygame.sprite.Sprite()
        self.window = None
        self.layer = layer
        self.position = position
        self.color = color
        self.size = size
        self.prev_pos = self.position
        self.rect = pygame.Rect(position.x, position.y, position.x+size.x, position.y+size.y)
        self.collision_sides = {"left":False, "right":False,
                                "bottom":False, "top":False}
        super().__init__(layer=self.layer, position=self.position)
    
    def detect_collisions(self):
        self.collision_sides = {"left":False, "right":False,
                                "bottom":False, "top":False}
        for j in range(1, 10+1):
            for i in self.window.layers[j]:
                if i != self:
                    side = self.get_collision_side(i)
                    if side != None:
                        self.collision_sides[side] = True
    
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
        self.window = window
        self.detect_collisions()
        pygame.draw.rect(window.surface, self.color, self.rect)
        super().render(window)
    
    def is_moving(self):
        return self.prev_pos == self.position
    
    def move(self, vec: pygame.Vector2):
        self.position = pygame.Vector2(self.position.x+vec.x, self.position.y+vec.y)
        self.rect.topleft = (self.position.x, self.position.y)
        self.prev_pos = self.position

class Image2D(Rect2D):
    def __init__(self, filename: str, layer=1, position=pygame.Vector2(0.0, 0.0)):#, size=pygame.Vector2(0.0, 0.0)):
        self.sprite = pygame.sprite.Sprite()
        self.debug = False
        self.layer = layer
        self.position = position
        self.name = filename
        self.image = pygame.image.load(self.name)
        self.rect = self.image.get_rect()
        self.image = self.image.convert_alpha()
        super().__init__(layer=self.layer, position=self.position)
    
    def render(self, window: Window):
        window.surface.blit(self.image, self.rect)
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
        pygame.mixer.music.load(file)
    
    def play(self):
        pygame.mixer.music.play()
