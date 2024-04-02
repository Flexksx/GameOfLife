import pygame
from Grid import Grid
from Cell import Cell
from InstrumentBar import InstrumentBar
import random


class Game:
    def __init__(self, cell_size: int = 50, x_size: int = 800, y_size: int = 800, randomize: bool = True, random_cells: float = 0.1) -> None:
        self.surface = pygame.display.set_mode((x_size, y_size+y_size//4))
        self.grid = Grid(cell_size=cell_size, x_size=x_size, y_size=y_size,
                         randomize=randomize, random_cells=random_cells, surface=self.surface)
        pygame.display.set_caption("Game of Life")
        pygame.display.flip()
        self.instrument_bar = InstrumentBar(x_pos=0, y_pos=y_size, x_size=x_size, y_size=y_size//4, surface=self.surface)
        self.x_size = x_size
        self.y_size = y_size
        self.paused = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.SysFont('arialblk', 36)

    def __write_pause_message(self):
        pause_message = self.font.render(
            "PAUSED. Press SPACE to Unpause", 1, (255, 255, 255))
        self.surface.blit(pause_message, (self.x_size//2-200, self.y_size//2))

    def run(self):
        self.paused = False
        self.grid.draw()
        self.grid.update()
        pygame.display.flip()

    def quit(self):
        pygame.quit()

    def pause(self):
        print("Pausing")
        self.paused = True
        self.grid.draw()
        self.__write_pause_message()
        pygame.display.flip()

    def __handle_cell_placing(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            pos = pygame.mouse.get_pos()
            row = pos[0]//self.grid.cell_size
            col = pos[1]//self.grid.cell_size
            if row < self.grid.rows and col < self.grid.cols:
                random_color = random.choice(['Red', 'Blue', 'Green'])
                self.grid.grid[row][col].birth(color=random_color)
                print(f"Cell placed at {row},{col} with color {random_color}")

    def __handle_cell_killing(self):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[2]:
            pos = pygame.mouse.get_pos()
            row = pos[0]//self.grid.cell_size
            col = pos[1]//self.grid.cell_size
            if row < self.grid.rows and col < self.grid.cols:
                self.grid.grid[row][col].kill()
                print(f"Cell killed at {row},{col}")



    def mainloop(self):
        while True:
            self.clock.tick(self.fps)
            self.instrument_bar.draw()
            self.grid.draw()
            states= self.instrument_bar.get_states()
            self.paused = states['pause']
            print(states)
            if self.paused:
                self.pause()
            else:
                self.run()
            for event in pygame.event.get():
                mouse_pressed = pygame.mouse.get_pressed()
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                    if event.key == pygame.K_q:
                        self.quit()
                elif mouse_pressed[0]:
                    self.__handle_cell_placing()
                elif mouse_pressed[2]:
                    self.__handle_cell_killing()
                    
                    
    # def handle_input(self):
    #     self.instrument_bar.draw()
    #     # self.handle_instrument_bar()
    #     previus_states = self.instrument_bar.get_states()
    #     states= self.instrument_bar.get_states()
    #     print(states)
    #     if states['pause']:
    #         print("Pausing")
    #         # self.pause()
    #     else:
    #         print("Resuming")
    #         # self.running = True
    #         # self.run()
    #     for event in pygame.event.get():
    #         mouse_pressed = pygame.mouse.get_pressed()
    #         if event.type == pygame.QUIT: 
    #             self.running = False
    #             self.quit()
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_SPACE:
    #                 if self.paused:
    #                     self.pause()
    #                 else:
    #                     self.run()
    #             if event.key == pygame.K_q:
    #                 self.quit()
    #         elif mouse_pressed[0]:
    #             self.__handle_cell_placing()
    #         elif mouse_pressed[2]:
    #             self.__handle_cell_killing()