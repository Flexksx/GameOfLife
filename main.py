import pygame
from Game import Game

pygame.init()

game = Game(cell_size=20, x_size=600,y_size=600, randomize=True, random_cells=0.3, iterations=50)
game.mainloop()