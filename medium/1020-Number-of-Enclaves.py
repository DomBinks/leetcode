class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # Look for land cells at the top and bottom borders of the grid
        for i in range(0, len(grid[0])):
            # If the top cell is a land cell
            if grid[0][i] == 1:
                grid[0][i] = -1
                self.mark(0, i, grid)
            # If the bottom cell is a land cell
            if grid[len(grid)-1][i] == 1:
                grid[len(grid)-1][i] = -1
                self.mark(len(grid)-1, i, grid)

        # Look for land cells on the left and right borders of the grid
        for i in range(1, len(grid)-1):
            # If the left cell is a land cell
            if grid[i][0] == 1:
                grid[i][0] = -1
                self.mark(i, 0, grid)
            # If the right cell is a land cell
            if grid[i][len(grid[i])-1] == 1:
                grid[i][len(grid[i])-1] = -1
                self.mark(i, len(grid[i])-1, grid)

        cells = 0 # Count the number of enclave cells
        # Loop over all the cells
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                # If the cell is 1 then it's an enclave
                if grid[i][j] == 1:
                    cells += 1 # Increment the number of cells

        return cells
    
    # Use 4 direction flood fill to mark adjacent land cells
    def mark(self, col: int, row: int, grid: List[List[int]]) -> None:
        # If there is a land cell to the left
        if col-1 >= 0 and grid[col-1][row] == 1:
            grid[col-1][row] = -1
            self.mark(col-1, row, grid)

        # If there is a land cell to the right
        if col+1 < len(grid) and grid[col+1][row] == 1:
            grid[col+1][row] = -1
            self.mark(col+1, row, grid)

        # If there is a land cell above
        if row-1 >= 0 and grid[col][row-1] == 1:
            grid[col][row-1] = -1
            self.mark(col, row-1, grid) 

        # If there is a land cell below
        if row+1 < len(grid[col]) and grid[col][row+1] == 1:
            grid[col][row+1] = -1
            self.mark(col, row+1, grid)
