import pygame
from Game import Game

pygame.init()

game = Game(cell_size=10, x_size=600,y_size=600, randomize=False, random_cells=0.5, iterations=50)
game.mainloop()