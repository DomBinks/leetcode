class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {} # Track the numbers seen
        for num in nums: # Loop over each number
            if num not in seen: # If it hasn't been seen yet
                seen[num] = 1 # Set the occurrences to 1
            else: # If it has been seen
                seen[num] += 1 # Increment the occurrences

        for key, value in seen.items(): # Go through each key value pair
            if value == 1: # If it only appears exactly once
                return key # Return the key as that's the number
