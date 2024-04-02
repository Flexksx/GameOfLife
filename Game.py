import pygame
from Grid import Grid
from Cell import Cell
from InstrumentBar import InstrumentBar
import random


class Game:
    def __init__(self, cell_size: int = 50, x_size: int = 800, y_size: int = 800, randomize: bool = True, random_cells: float = 0.1, iterations:int=None) -> None:
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
        self.iterations = iterations
        self.font = pygame.font.SysFont('arialblk', 36)

    def __write_pause_message(self):
        pause_message = self.font.render(
            "PAUSED. Press SPACE to Unpause", 1, (255, 255, 255))
        self.surface.blit(pause_message, (self.x_size//2-200, self.y_size//2))

    def run(self):
        self.paused = False
        self.grid.update()
        # pygame.display.flip()

    def quit(self):
        pygame.quit()

    def pause(self):
        self.paused = True
        self.grid.draw()
        self.__write_pause_message()
        # pygame.display.flip()

    def __handle_cell_placing(self,color=None, is_high=False):
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            pos = pygame.mouse.get_pos()
            row = pos[0]//self.grid.cell_size
            col = pos[1]//self.grid.cell_size
            if row < self.grid.rows and col < self.grid.cols:
                if color is None:
                    color = random.choice(
                        ['Red', 'Blue', 'Green', 'Black', 'White','Magenta','Yellow','Cyan'])
                self.grid.grid[row][col].birth(color=color, is_high=is_high)
                print(f"Cell placed at {row,col} with color {self.grid.grid[row][col].color} with high {self.grid.grid[row][col].is_high}")

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
        self.paused = True
        tick_count = 0
        if self.iterations is not None:
            for i in range(self.iterations):
                self.run()
                
        while True:
            self.clock.tick(self.fps)
            self.instrument_bar.draw()
            self.grid.draw()
            states= self.instrument_bar.get_states()
            self.paused = states['pause']
            if self.paused:
                self.pause()
            else:
                tick_count += 1
                if tick_count % 7 == 0:
                    self.run()
            for event in pygame.event.get():
                mouse_pressed = pygame.mouse.get_pressed()
                if event.type == pygame.QUIT:
                    self.running = False
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                        self.instrument_bar.set_states({'pause':self.paused})
                    if event.key == pygame.K_q:
                        self.quit()
                    if event.key == pygame.K_MINUS:
                        self.fps -= 5
                    if event.key == pygame.K_EQUALS:
                        self.fps += 5
                elif mouse_pressed[0]:
                    if states['red']:
                        self.__handle_cell_placing(color='Red', is_high=states['high'])
                    elif states['blue']:
                        self.__handle_cell_placing(color='Blue', is_high=states['high'])
                    elif states['green']:
                        self.__handle_cell_placing(color='Green', is_high=states['high'])
                    elif states['white']:
                        self.__handle_cell_placing(color='White', is_high=states['high'])
                    else:
                        self.__handle_cell_placing(is_high=states['high'])
                elif mouse_pressed[2]:
                    self.__handle_cell_killing()
            pygame.display.flip()
                    
                    