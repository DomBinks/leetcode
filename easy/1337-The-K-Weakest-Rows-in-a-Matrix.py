from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Returns the k weakest rows of the provided matrix"""
        rows = [0] * len(mat) # Stores the weakness of each row

        for i in range(len(mat)): # For every row in the matrix
            for j in mat[i]: # For every element in the row
                rows[i] += j # Add the value to the weakness array

        weakest = [] # Stores the indicies of the k weakest rows
        for i in range(k): # Loop k times
            weak = 99999999 # Stores the weakest value
            index = 99999999 # Stores the index of the weakest value

            for j in range(len(rows)): # For each row
                if j in weakest: # Skip the row if it is already one
                    continue     # of the weakest

                if rows[j] < weak: # If the current row is the weakest
                    weak = rows[j] # Update weakest value
                    index = j # Update index of weakest value
            
            weakest.append(index)

        return weakest