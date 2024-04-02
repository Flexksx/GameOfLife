import pygame
import random
from Grid import Grid

class InstrumentBar:
    def __init__(self, x_pos=None, y_pos=None, x_size=None, y_size=None, surface=None ) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_size = x_size
        self.y_size = y_size
        self.surface = surface
        self.pause_button()
        
    def draw(self):
        pygame.draw.rect(self.surface, (255,255,255), (self.x_pos, self.y_pos, self.x_size, self.y_size))
        pygame.display.flip()
        self.pause_button.draw()
        
    def pause_button(self):
        self.pause_button = Button(x=self.x_pos+10, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(200,200,200), text='Pause')
    
    def get_states(self):
        return {'pause':self.pause_button.get_state()}
        
class Button:
    def __init__(self, x=None,y=None,xsize=None,ysize=None, color=None, text=None, surface=None) -> None:
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('arialblk', 15)
        self.surface = surface
        self.message = self.font.render(self.text, 1, (0,0,0))
        self.current_state = False
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.xsize, self.ysize))
        self.surface.blit(self.message, (self.x+10, self.y+10))
        pygame.display.flip()
        
    def get_state(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.x <= mouse_pos[0] <= self.x+self.xsize and self.y <= mouse_pos[1] <= self.y+self.ysize:
                self.current_state = not self.current_state
        return self.current_state