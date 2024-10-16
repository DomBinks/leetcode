class Solution:
    def countBits(self, n: int) -> List[int]:
        # For each number from 0 to n inclusive
        # Convert the number to a binary string
        # Count the number of 1s in the string
        # Add the count to an output list
        # Return the output list
        return [bin(i).count('1') for i in range(0,n+1)]
