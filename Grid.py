import pygame
import random
from Cell import Cell


class Grid:
    def __init__(self, cell_size: int = None, x_size: int = None, y_size: int = None, surface: pygame.display = None, randomize: bool = True, random_cells: float = 0.5) -> None:
        self.x_size = x_size
        self.y_size = y_size
        self.surface = surface
        self.cell_size = cell_size
        self.rows = self.x_size//self.cell_size
        self.cols = self.y_size//self.cell_size
        self.grid = [[0 for _ in range(self.rows)] for _ in range(self.cols)]
        self.__init_grid(randomize=randomize, random_cells=random_cells)
        print(self.rows, self.cols)

    def draw(self):
        for row in range(self.rows):
            for col in range(self.cols):
                pygame.draw.rect(
                    self.surface, self.grid[row][col].color, self.grid[row][col].rect)
        pygame.display.flip()

    def __init_grid(self, randomize: bool = True, random_cells: float = 0.5):
        for row in range(self.rows):
            for col in range(self.cols):
                if randomize == True:
                    alive_cell = random.choices([True, False], weights=[
                                                random_cells, 1-random_cells], k=1)[0]
                    if alive_cell:
                        random_color = random.choice(
                            ['Red', 'Blue', 'Green', 'Black', 'White'])
                        high = random.choice([True, False])
                        self.grid[row][col] = Cell(color=random_color, pos=(
                            row*self.cell_size, col*self.cell_size), size=self.cell_size, is_alive=True, is_high=high)
                    else:
                        self.grid[row][col] = Cell(color=(0, 0, 0), pos=(
                            row*self.cell_size, col*self.cell_size), size=self.cell_size, is_alive=False)
                else:
                    self.grid[row][col] = Cell(color=(0, 0, 0), pos=(
                        row*self.cell_size, col*self.cell_size), size=self.cell_size, is_alive=False)

    def update(self):
        cells_to_kill = []
        cells_to_birth = {}
        for row in range(self.rows):
            for col in range(self.cols):
                current_cell = self.grid[row][col]
                count_neighbours, list_neighbours = 0, []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        try:
                            if i == 0 and j == 0:
                                continue
                            if row+i >= 0 and col+j >= 0:
                                neighbour = self.grid[row+i][col+j]
                                if neighbour.is_alive:
                                    count_neighbours += 1
                                    list_neighbours.append(neighbour)
                        except IndexError:
                            continue
                if self.grid[row][col].is_alive:
                    count_high_neighbours = 0
                    for neighbour in list_neighbours:
                        if neighbour.is_high:
                            count_high_neighbours += 1
                    if count_neighbours < 2:
                        if count_high_neighbours > 0:
                            cells_to_birth.update(
                                {self.grid[row][col]: [count_neighbours, list_neighbours]})
                        else:
                            cells_to_kill.append(self.grid[row][col])
                    if count_neighbours > 3:
                        cells_to_kill.append(self.grid[row][col])
                elif not self.grid[row][col].is_alive:
                    if count_neighbours == 3:
                        cells_to_birth.update(
                            {self.grid[row][col]: [count_neighbours, list_neighbours]})
        for cell in cells_to_kill:
            cell.kill()
        for cell in cells_to_birth.keys():
            cell.birth(
                neighbour_count=cells_to_birth[cell][0], neighbour_list=cells_to_birth[cell][1])
        self.zone()

    def zone(self):
        interval = 3
        self.x_start = self.rows//2-interval
        self.y_start = self.cols//2-interval
        self.x_end = self.rows//2+interval
        self.y_end = self.cols//2+interval
        neighbours = []
        for row in range(self.x_start, self.x_end):
            for col in range(self.y_start, self.y_end):
                random_color = random.choice(
                    ['Red', 'Blue', 'Green', 'White','Magenta','Yellow','Cyan'])
                self.grid[row][col].birth(color=random_color, is_high=True)
                neighbours.append(self.grid[row][col])
        for row in range(self.rows):
            for col in range(self.cols):
                if row >= self.x_start and row <= self.x_end or col >= self.y_start and col <= self.y_end:
                    self.grid[row][col].birth(
                        neighbour_list=neighbours)