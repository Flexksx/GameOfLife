import pygame
import random

class Cell:
    def __init__(self,color=None,pos:tuple=None,size:int=None, is_alive:bool=None, is_high:bool=False) -> None:
        if type(color)==str:
            self.__handle_random_color(color)
        elif type(color)==tuple:
            self.color = color
        elif color is None:
            self.color = (0,0,0)
        self.is_high=is_high
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(self.pos[0],self.pos[1],self.size,self.size)
        self.is_alive = is_alive
        if self.is_alive==False:
            self.color = (0,0,0)
        
    
    def __repr__(self) -> str:
        return f'{int(self.is_alive)}'
    
    def __handle_random_color(self, color:str=None):
        if color is not None:
            if color == 'Red':
                self.color = (255,0,0)
            elif color == 'Blue':
                self.color = (0,0,255)
            elif color == 'Green':
                self.color = (0,255,0)
            elif color == 'Black':
                self.color = (0,0,0)
            elif color == 'White':
                self.color = (255,255,255)
    
    def update(self):
        # if self.is_alive==False:
            # self.color = (0,0,0)
        if self.color[0]<50 and self.color[1]<50 and self.color[2]<50:
            self.kill()
        if self.is_high:
            print('High')
            
    def birth(self, neighbour_count:int=None, neighbour_list:list=None, color:str=None, is_high:bool=None):
        if neighbour_count is not None and neighbour_list is not None:
            self.__birth_by_neighbour(neighbour_list=neighbour_list)
        elif color is not None:
            self.__birth_by_click(color=color,is_high=is_high)
            
    def kill(self):
        self.is_alive = False
        self.is_high=False
        # self.color = (0,0,0)
        
    def __birth_by_neighbour(self, neighbour_list:list=None):
        self.is_alive = True
        if self.is_high:
            print('High')
        new_color_red=0
        new_color_green=0
        new_color_blue=0
        red_division=1
        green_division=1
        blue_division=1
        for neighbour in neighbour_list:
            new_color_red+=neighbour.color[0]
            new_color_green+=neighbour.color[1]
            new_color_blue+=neighbour.color[2]
            red_division+=1
            green_division+=1
            blue_division+=1
        
        if not self.is_high and self.is_alive: 
            new_color_red = new_color_red//red_division
            new_color_green = new_color_green//green_division
            new_color_blue = new_color_blue//blue_division
            
        new_color_red = min(255,new_color_red)
        new_color_green = min(255,new_color_green)
        new_color_blue = min(255,new_color_blue)
        self.color = (new_color_red,new_color_green,new_color_blue)
        
    def __birth_by_click(self, color:tuple[int,int,int]=None, is_high:bool=False):
        self.is_alive = True
        self.is_high = is_high
        if color is not None:
            self.__handle_random_color(color)
        else:
            random_color = random.choice(['Red','Blue','Green','Black', 'White'])
            self.__handle_random_color(random_color)