# Use cases -- Chess board, tic-tac-toe, nqueens

"""
Always deal with grids as rows and column; attempt to do them as
X and Y values could go very wrong
"""

# Python lists are references and can lead to bugs 🐞
def wrong2DGrid(rows, cols, fill_value=0):
    # This may seem correct at first; but don't do this as 
    # Python lists are references and will result in bugs
    column = [fill_value] * cols
    return [column] * rows

# Do it properly, use this as a helper ✅
def create2DGrid(rows, cols, fill_value=0):
    """This creates a 2D grid efficiently

    Args:
        rows (int): number of rows
        cols (int): number of columns
        fill_value (int, optional): Init values of the grid. Defaults to 0.

    Returns:
        List[List[any]]: A 2D grid
    """
    return [ [fill_value for _ in range(cols)] for _ in range(rows)]


wrong = wrong2DGrid(2,2)
wrong[1][1] = "!"
print(wrong)
"""
[[0, '!'], [0, '!']]
"""

right = create2DGrid(2,2)
right[1][1] = "!"
print(right)
"""
[[0, 0], [0, '!']]
"""









"""
Why create a 2D grid when you can store as a single grid
"""

class MultiDimensionGrid: # Good abstraction 😍

    def __init__(self, rows, cols, fill_value=0):
        super().__init__()
        self.nrows = rows
        self.ncols = cols
        self.store = [0] * (cols * rows)
    
    def get_oneD_index(self, row, col):
        """Converts row and col to one dimension array index

        Args:
            row (int): row index
            col (int): col index

        Returns:
            int: the index in the one dimension array
        """
        return (row * self.nrows) + col
    
    def set_val(self, row: int, col: int, value: any) -> None:
        # This is 0 indexed; so if you have 5 rows and 5 columns 
        # (4, 4) is bottom right
        assert 0 <= row < self.nrows
        assert 0 <= col < self.ncols
        
        index_to_put = self.get_oneD_index(row, col)
        self.store[index_to_put] = value
    
    def get_val(self, row: int, col: int) -> any:
        assert 0 <= row < self.nrows
        assert 0 <= col < self.ncols
        
        index_to_get = self.get_oneD_index(row, col)
        return self.store[index_to_put]
    

    def __str__(self):
        out = []
        for i,value in enumerate(self.store):
            if i % self.nrows == 0 and i != 0:
                out.append(f" --row {(i // self.nrows) - 1} end\n")
            out.append(str(value) + " ")
        return "".join(out)



if __name__ == "__main__":
    grid = MultiDimensionGrid(2, 2)
    grid.set_val(0, 1, 8)
    print(grid)
    """
    0 8  --row 0 end
    0 0 
    """