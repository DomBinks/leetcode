class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0 # Count the number of ships

        # Loop over each cell
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == "X": # If a ship is in that cell
                    ships += 1 # Increment the count
                    board[i][j] = "M" # Mark that cell as checked
                    self.markAround("", j, i, board) # Mark the cells of the same ship

        return ships

    # Marks the cells of the same ship by checking around for other unmarked cells
    def markAround(self, direction: str, x: int, y: int, board: List[List[str]]) -> None:
        # If the direction is unknown or horizontal check horizontal cells
        if direction == "" or direction == "H":
            # If there is a cell to the left
            if x-1 >= 0:
                # Check that cell
                if board[y][x-1] == "X":
                    board[y][x-1] = "M"
                    self.markAround("H", x-1, y, board)
    
            # If there is a cell to the right
            if x+1 < len(board[y]):
                # Check that cell
                if board[y][x+1] == "X":
                    board[y][x+1] = "M"
                    self.markAround("H", x+1, y, board)

        # If the direction is unknown or vertical check vertical cells
        if direction == "" or direction == "V":
            # If there is a cell above
            if y-1 >= 0:
                # Check that cell
                if board[y-1][x] == "X":
                    board[y-1][x] = "M"
                    self.markAround("V", x, y-1, board)

            # If there is a cell below
            if y+1 < len(board):
                # Check that cell
                if board[y+1][x] == "X":
                    board[y+1][x] = "M"
                    self.markAround("V", x, y+1, board)
