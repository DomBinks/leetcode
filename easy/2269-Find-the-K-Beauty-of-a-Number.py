class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numS = str(num) # Convert the input num to a string
        total = 0 # Keep track of the running total
        for i in range(k,len(numS)+1): # For each substring of size k
            x = int(numS[i-k:i]) # Get the integer value of the substring
            if x != 0 and num % x == 0: # If the condition is satisfied
                total += 1 # Increment total

        return total
