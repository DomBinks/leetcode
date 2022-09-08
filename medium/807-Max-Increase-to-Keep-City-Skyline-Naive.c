#define min(x,y) (x < y ? x : y)

// Returns the maximum total height increase while keeping the skyline
// the same
int maxIncreaseKeepingSkyline(int** grid, int gridSize, int* gridColSize)
{
    int *maxRow = calloc(gridSize, sizeof(int)); // Max value in each row
    int *maxCol = calloc(gridSize, sizeof(int)); // Max value in each column
    int out = 0; // Output value

    for(int i = 0; i < gridSize; i++)
    {
        for(int j = 0; j < gridSize; j++) // For each building in the grid
        {
            if(grid[i][j] > maxRow[i]) // Check for new max row value
            {
                maxRow[i] = grid[i][j];
            }
            
            if(grid[i][j] > maxCol[j]) // Check for new max column value
            {
                maxCol[j] = grid[i][j];
            }
        }
    }

    for(int i = 0; i < gridSize; i++)
    {
        for(int j = 0; j < gridSize; j++) // For each building in the grid
        {
            // New building height is the lower value of the max row
            // and column value 
            // Add the difference of the new building height and the
            // exisiting height to the running total
            out += (min(maxRow[i], maxCol[j]) - grid[i][j]);
        }
    }

    free(maxRow);
    free(maxCol);
    return out;
}