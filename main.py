import pygame
from Game import Game

pygame.init()

game = Game(cell_size=20, x_size=800,y_size=800, randomize=True, random_cells=0.3)
game.mainloop()