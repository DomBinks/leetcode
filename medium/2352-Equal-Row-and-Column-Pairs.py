class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        seen = {} # Seen columns
        count = 0 # Number of pairs
        new_grid = [] # Transposed grid
        
        # Create an array to store the transposed gird
        for i in range(len(grid)):
            new_grid += [[None]]
            for j in range(len(grid) - 1):
                new_grid[i] += [None]

        # Transpose the grid
        for i in range(len(new_grid)):
            for j in range(len(new_grid)):
                new_grid[i][j] = grid[j][i]
            
            # Add the column (now row) to seen
            if str(new_grid[i]) not in seen:
                seen[(str(new_grid[i]))] = 1
            else:
                seen[(str(new_grid[i]))] += 1

        # For each row in grid
        for row in grid:
            # Check if a columns was seen with the same value
            if str(row) in seen:
                # Increment count by the amount of columns that
                # are the same as this row
                count += seen[str(row)]
                
        return count
