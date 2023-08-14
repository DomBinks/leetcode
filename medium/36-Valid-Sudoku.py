class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = [] # Stores the lists of numbers to check for duplicates

        # For each row and column
        for i in range(0, 9):
            row = board[i] # Get the row
            col = [r[i] for r in board] # Get the column

            check.append(row) # Add the row to the list to check
            check.append(col) # Add the column to the list to check

        # For each row of boxes
        for i in range(0, 9, 3):
            a = [] # Stores the left box
            b = [] # Stores the middle box
            c = [] # Stores the right box
            for j in range(i, i+3): # For each row in the box
                # Add the first 3 numbers to the left box
                a.append(board[j][0])
                a.append(board[j][1])
                a.append(board[j][2])

                # Add the middle 3 numbers to the middle box
                b.append(board[j][3])
                b.append(board[j][4])
                b.append(board[j][5])

                # Add the last 3 numbers to the right box
                c.append(board[j][6])
                c.append(board[j][7])
                c.append(board[j][8])

            # Add the boxes to the list to check
            check.append(a)
            check.append(b)
            check.append(c)

        # For each list in the list to check
        for s in check:
            seen = {} # Tracks the numbers seen

            for c in s: # For each number
                # If it's already been seen and isn't the blank space
                if c in seen and c != '.':
                    return False
                # If it hasn't been seen
                else:
                    # Set this number to seen
                    seen[c] = True

        # If there are no duplicates
        return True
