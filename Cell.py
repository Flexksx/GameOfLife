import pygame
import random

class Cell:
    def __init__(self,color=None,pos:tuple=None,size:int=None, is_alive:bool=None) -> None:
        if type(color)==str:
            self.__handle_random_color(color)
        elif type(color)==tuple:
            self.color = color
        elif color is None:
            self.color = (0,0,0)
            
        
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
        if self.is_alive==False:
            self.color = (0,0,0)
        if self.color[0]<50 and self.color[1]<50 and self.color[2]<50:
            self.kill()
            
    def birth(self, neighbour_count:int=None, neighbour_list:list=None, color:str=None):
        if neighbour_count is not None and neighbour_list is not None:
            self.__birth_by_neighbour(neighbour_count=neighbour_count, neighbour_list=neighbour_list)
        elif color is not None:
            self.__birth_by_click(color=color)
            
    def kill(self):
        self.is_alive = False
        self.color = (0,0,0)
        
    def __birth_by_neighbour(self, neighbour_count:int=None, neighbour_list:list=None):
        self.is_alive = True
        
        new_color_red=0
        new_color_green=0
        new_color_blue=0
        
        for neighbour in neighbour_list:
            new_color_red+=neighbour.color[0]
            new_color_green+=neighbour.color[1]
            new_color_blue+=neighbour.color[2]
        
        new_color_red = new_color_red//neighbour_count
        new_color_green = new_color_green//neighbour_count
        new_color_blue = new_color_blue//neighbour_count
        new_color_red = min(255,new_color_red)
        new_color_green = min(255,new_color_green)
        new_color_blue = min(255,new_color_blue)
        self.color = (new_color_red,new_color_green,new_color_blue)
        
    def __birth_by_click(self, color:tuple[int,int,int]=None):
        self.is_alive = True
        if color is not None:
            self.__handle_random_color(color)
        else:
            random_color = random.choice(['Red','Blue','Green','Black', 'White'])
            self.__handle_random_color(random_color)