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
        self.red_color_button()
        self.blue_color_button()
        self.green_color_button()
        self.white_color_button()
        self.high_state_button()
    def draw(self):
        pygame.draw.rect(self.surface, (255,255,255), (self.x_pos, self.y_pos, self.x_size, self.y_size))
        # pygame.display.flip()
        self.pause_button.draw()
        self.red_color_button.draw()
        self.blue_color_button.draw()
        self.green_color_button.draw()
        self.white_color_button.draw()
        self.high_state_button.draw()
        
    def pause_button(self):
        self.pause_button = Button(x=self.x_pos+10, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(200,200,200), text='Pause', init_state=True)
    
    def red_color_button(self):
        self.red_color_button = Button(x=self.x_pos+70, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(255,0,0), text='Red')
    
    def blue_color_button(self):
        self.blue_color_button = Button(x=self.x_pos+130, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(0,0,255), text='Blue')
    
    def green_color_button(self):
        self.green_color_button = Button(x=self.x_pos+190, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(0,255,0), text='Green')
    
    def white_color_button(self):
        self.white_color_button = Button(x=self.x_pos+250, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(255,255,255), text='White')
    
    def high_state_button(self):
        self.high_state_button = Button(x=self.x_pos+310, y=self.y_pos+10, xsize=50, ysize=50,surface=self.surface, color=(255,0,255), text='High')
    
    
    def get_states(self):
        states_dict = {}
        pause = self.pause_button.get_state()
        red = self.red_color_button.get_state()
        blue = self.blue_color_button.get_state()
        green = self.green_color_button.get_state()
        white = self.white_color_button.get_state()
        high = self.high_state_button.get_state()
        states_dict['pause'] = pause
        states_dict['red'] = red
        states_dict['blue'] = blue
        states_dict['green'] = green
        states_dict['white'] = white
        states_dict['high'] = high
        if red and not blue and not green and not white:
            states_dict['red'] = True
            states_dict['blue'] = False
            states_dict['green'] = False
            states_dict['white'] = False
        elif blue and not red and not green and not white:
            states_dict['blue'] = True
            states_dict['red'] = False
            states_dict['green'] = False
            states_dict['white'] = False
        elif green and not red and not blue and not white:
            states_dict['green'] = True
            states_dict['red'] = False
            states_dict['blue'] = False
            states_dict['white'] = False
        elif white and not red and not blue and not green:
            states_dict['white'] = True
            states_dict['red'] = False
            states_dict['blue'] = False
            states_dict['green'] = False
        elif not red and not blue and not green and not white:
            states_dict['red'] = False
            states_dict['blue'] = False
            states_dict['green'] = False
            states_dict['white'] = False
        return states_dict
        
        
    def set_states(self, states:dict):
        if 'pause' in states:
            self.pause_button.set_state(states['pause'])
        if 'red' in states:
            self.pause_button.set_state(states['red'])
class Button:
    def __init__(self, x=None,y=None,xsize=None,ysize=None, color=None, text=None, surface=None, init_state=None) -> None:
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.text = text
        self.font = pygame.font.SysFont('arialblk', 15)
        self.surface = surface
        if init_state is not None:
            self.current_state = init_state
        else:
            self.current_state = False
            
    def draw(self):
        if not self.current_state:
            pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.xsize, self.ysize))
            self.message = self.font.render(self.text, 1, (0,0,0))
            self.surface.blit(self.message, (self.x+10, self.y+10))
        else:
            pygame.draw.rect(self.surface, (255,255,255), (self.x, self.y, self.xsize, self.ysize))
            self.message = self.font.render(self.text, 1, self.color)
            self.surface.blit(self.message, (self.x+10, self.y+10))
        # pygame.display.flip()
        
    def get_state(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.x <= mouse_pos[0] <= self.x+self.xsize and self.y <= mouse_pos[1] <= self.y+self.ysize:
                self.current_state = not self.current_state
        return self.current_state
    
    def set_state(self, state:bool):
        self.current_state = state
        return self.current_state
    