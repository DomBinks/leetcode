class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # Stores the minimum x and y coordinates of a range
        x = m
        y = n

        # For each operation
        for op in ops:
            # Update the minimum x and y coordinate
            x = min(x, op[0])
            y = min(y, op[1])

        # Return the product of the minimum x and y coordinates
        # as this area is covered by all ranges
        return x * y
