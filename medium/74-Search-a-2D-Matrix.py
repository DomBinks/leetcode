class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Base case of null matrix
        if matrix == [[]] or target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return False

        # Binary search for the row
        low = 0 # low pointer
        high = len(matrix) - 1 # high pointer
        r = 0 # the resultant row

        # While there is a range of rows to pick from
        while low <= high:
            # Find the mid row
            mid = low + ((high - low) // 2)

            # If the target is less than first in this row
            if matrix[mid][0] > target:
                # Target is in a row before this row
                high = mid - 1
            # If the target is greater than the last in this row
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                # Target is in a row after this row
                low = mid + 1
            # Otherwise target is in this row
            else:
                # Set r to this row
                r = mid
                break

        # Binary search for the columns
        row = matrix[r]
        low = 0
        high = len(row) - 1

        # While there is a range to pick from
        while low <= high:
            # Get the midpoint
            mid = low + ((high - low) // 2)

            # Check if the midpoint is the target
            if row[mid] == target:
                return True
            # If the midpoint is below
            elif row[mid] < target:
                # Lowest possible is next greatest
                low = mid + 1
            # If the midpoint is above
            else:
                # Highest possible is next lowest
                high = mid - 1
        
        return False
