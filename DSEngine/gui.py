import pygame as pg
from DSEngine.etypes import Type2D, Window
from pygame.locals import *

class InputBox(Type2D):
    def __init__(self, layer="GUI", position=pg.Vector2(0.0, 0.0), size=pg.Vector2(100.0, 100.0), text=''):
        self.COLOR_INACTIVE = pg.Color('lightskyblue3')
        self.COLOR_ACTIVE = pg.Color('dodgerblue2')
        self.FONT = pg.font.Font(None, 32)
        self.rect = pg.Rect(position.x, position.y, position.x+size.x, position.x+size.y)
        self.position = position
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.layer = layer
        self.txt_surface = self.FONT.render(text, True, self.color)
        super().__init__(layer=self.layer, position=self.position)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    def update(self, window: Window):
        # Resize the box if the text is too long.
        pass

    def render(self, window: Window):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        super().render(window)
        window.surface.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(window.surface, self.color, self.rect, 2)
