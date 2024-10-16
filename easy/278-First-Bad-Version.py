# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1 # Lower bound
        r = n # Upper bound
        
        i = round(n / 2) # Get the middle number

        # If the 1st number is bad
        if isBadVersion(1):
            return 1

        while True:
            # If the current middle number is bad
            if isBadVersion(i):
                # Set this number as the upper bound
                r = i
            # If the current middle number isn't bad
            else:
                # Set this number as the lower bound
                l = i
            
            # Set the middle number to be the middle of the 2 bounds
            i = l + floor((r - l) / 2)

            # If the middle number is the same as the left bound i.e.
            # we've found the last good number and the first bad number
            if i == l:
                break

        # Return the 1st bad number
        # (l is the last good number)
        return r
