'''
    Given an NxN grid with Red and Green boxes
        -   Green boxes denote open areas   
        -   Red boxes denote closed areas
    
    Percolation means - you have path of Green boxes such that it connects the top to bottom

    Start with a grid with all boxes and randomly open a box such that percolation is created.
    Find average percentage of boxes to be opened for the grid to percolate 
'''
import random
from colorama import init, Style, Fore, Back

init()


class Cell:
    def __init__(self: object, row: int = None, col: int = None, virtual: str = None) -> object:
        if row is not None and col is not None:
            self.value = '*'  # Empty value means the cell is open
            self.row = row   # Row num between 1 and Grid.size
            self.col = col   # Col num between 1 and Grid.size

            # Pos is the cell position in flat grid
            self.pos = (self.row - 1) * Grid.size + self.col

            # Parent is the immediate upper node for the cell (when arranged in heap structure)
            self.parent = self.pos

        # Virtual Top node is not part of grid, but virtually connects all cells of the top row
        elif virtual == 'top':
            self.value = 'T'
            self.row = self.col = self.pos = self.parent = 0

        # Virtual Bottom node is not part of grid, but virtually connects all cells of the bottom row
        elif virtual == 'bottom':
            self.value = 'B'
            self.row = self.col = self.pos = self.parent = Grid.size ** 2 + 1

        # Number of open cells that are connected to this cells (Same connected group)
        self.num_connected = 0

    @property
    def open(self: object) -> bool:
        # Returns True when a particular cell is open
        return self.value == ' '

    def open_cell(self: object) -> None:
        self.value = ' '
        self.num_connected = 1

    def __str__(self: object) -> str:
        return self.value


class Grid:
    # 30x30 grid
    size = 30

    def __init__(self: object) -> object:
        # Init NxN grid with all cells as closed (value='*')
        self.square = [[Cell(row+1, col+1)
                        for col in range(Grid.size)]
                       for row in range(Grid.size)]

        # Create top and bottom virtual nodes
        self.top_cell = Cell(virtual='top')
        self.bottom_cell = Cell(virtual='bottom')

        # Initialize num of open cells in the grid
        self.num_of_open_cells = 0
        self.virtual_connection()

    def virtual_connection(self: object) -> None:
        # Virtually connect all top cells to top virtual node and bottom cells to bottom node
        for col in range(Grid.size):
            self.square[0][col].parent = self.top_cell.parent
            self.square[Grid.size-1][col].parent = self.bottom_cell.parent

    @property
    def open_cells(self: object) -> list:
        # Returns all open cells in grid as a flat list
        return [self.square[row][col]
                for col in range(Grid.size)
                for row in range(Grid.size)
                if self.square[row][col].open]

    @property
    def closed_cells(self: object) -> list:
        # Returns all closed cells in grid as a flat list
        return [self.square[row][col]
                for col in range(Grid.size)
                for row in range(Grid.size)
                if not self.square[row][col].open]

    def parent_cell(self: object, cell: object) -> object:
        # Returns the parent of the input cell

        # Get row and col number for the parent of input cell
        parent_row = (cell.parent-1) // Grid.size
        parent_col = (cell.parent-1) % Grid.size

        # If input cell is from top row, return the top virtual node
        if parent_row < 0 or parent_col < 0:
            return self.top_cell

        # If input cell is from bottom row, return the bottom virtual node
        elif parent_row >= Grid.size or parent_col >= Grid.size:
            return self.bottom_cell

        # Else return the parent cell
        else:
            return self.square[parent_row][parent_col]

    def root(self: object, cell: object) -> object:
        # Returns the ultimate parent for the cell (the topmost node for the cell when arranged in heap structure)

        # A cell is the topmost node, if the cell is its own parent
        while cell.parent != cell.pos:
            # Traverse up the heap, using parent of cell, until the root is found
            parent_cell = self.parent_cell(cell)
            cell.parent = parent_cell.parent
            cell = parent_cell

        return cell

    def union(self: object, cell1: object, cell2: object) -> None:
        # Connects two cells in the input (Makes their root common)

        # Find the root of two cells, Return if they have already same root
        root1 = self.root(cell1)
        root2 = self.root(cell2)
        if root1 == root2:
            return

        # If root of first cell is a virtual node, make the root of second cell as same
        # Adjust the connected component count accordingly
        if root1 in (self.top_cell, self.bottom_cell):
            root2.parent = root1.parent
            root1.num_connected += root2.num_connected

        # If root of second cell is a virtual node, make the root of second cell as same
        # Adjust the connected component count accordingly
        elif root2 in (self.top_cell, self.bottom_cell):
            root1.parent = root2.parent
            root2.num_connected += root1.num_connected

        # Else connect the smaller group to larger one
        elif root1.num_connected < root2.num_connected:
            root1.parent = root2.parent
            root2.num_connected += root1.num_connected
        else:
            root2.parent = root1.parent
            root1.num_connected += root2.num_connected

    @property
    def percolates(self: object) -> bool:
        # Returns true, if one of the top row cells is connected to one of the bottom row cells
        return self.root(self.top_cell) == self.root(self.bottom_cell)

    def adjacent_open_cells(self: object, cell: object) -> list:
        # Returns a list of open cells that are directly connected (adjacent) to input cell
        adj_cells = []
        cell_row = (cell.pos-1) // Grid.size
        cell_col = (cell.pos-1) % Grid.size

        for row in range(cell_row-1, cell_row+2):
            for col in range(cell_col-1, cell_col+2):
                if 0 <= row < Grid.size and 0 <= col < Grid.size:
                    if (row == cell_row and col != cell_col) or \
                            (row != cell_row and col == cell_col):
                        if self.square[row][col].open:
                            adj_cells.append(self.square[row][col])
        return adj_cells

    def print(self):
        # Prints the grid as NxN boxes of Green and Red color
        # Green is open cell and Red is closed cell
        HORZ = ' --' * Grid.size
        for row in range(Grid.size):
            print(Fore.BLACK + HORZ)
            for col in range(Grid.size):
                if col == Grid.size - 1:
                    if str(self.square[row][col]) == '*':
                        print(Fore.BLACK + Back.BLACK + '|', Back.RED +
                              '  ', Fore.BLACK + Back.BLACK + '|', sep='')
                    else:
                        print(Fore.BLACK + Back.BLACK + '|', Back.GREEN +
                              '  ', Fore.BLACK + Back.BLACK + '|', sep='')
                else:
                    if str(self.square[row][col]) == '*':
                        print(Fore.BLACK + Back.BLACK + '|', Back.RED +
                              '  ', sep='', end='')
                    else:
                        print(Fore.BLACK + Back.BLACK + '|', Back.GREEN +
                              '  ', sep='', end='')
        print(HORZ)


class Percolation:
    def __init__(self: object) -> object:
        # Initialize the grid
        self.grid = Grid()

        # Randomly open a cell until the grid percolates (top cell connected to bottom cell)
        while not self.grid.percolates:
            cell = random.choice(self.grid.closed_cells)
            cell.open_cell()
            for adjc in self.grid.adjacent_open_cells(cell):
                self.grid.union(cell, adjc)

        self.grid.print()
        print(Style.RESET_ALL)

    def percent(self: object) -> float:
        # Returns the percent of open cells in the entire grid
        return len(self.grid.open_cells) / (Grid.size ** 2)


if __name__ == '__main__':
    percolate = Percolation()
    print(f'Percolation pct: {percolate.percent()}')
