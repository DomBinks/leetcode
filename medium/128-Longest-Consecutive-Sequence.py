class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {} # Stores numbers seen
        lRanges = {} # Stores ranges (key: left, value: right)
        rRanges = {} # Stores ranges (key: right, value: left)

        # For each number
        for i in nums:
            # Skip it if seen
            if i in seen:
                continue
            else:
                seen[i] = True

            if i+1 in lRanges: # If there is the number to the right
                r = lRanges[i+1] # Get the furthest right from that number
                lRanges.pop(i+1) # Remove the range from the number to the right
                lRanges[i] = r # Add the range from i
                rRanges[r] = i # Set the range from the furthest right to i

                if i-1 in rRanges: # If if there is a number to the left
                    nl = rRanges[i-1] # Get the furthest left from that number
                    rRanges.pop(i-1) # Remove the range for the number to the left
                    rRanges[r] = nl # Add the range from the furthest right
                    lRanges[nl] = r # Set the range from the furthest left to the furthest right
                

            elif i-1 in rRanges: # If there is a number to the left
                l = rRanges[i-1] # Get the furthest left from that number
                rRanges.pop(i-1) # Remove the range from the number to the left
                rRanges[i] = l # Add the range from i
                lRanges[l] = i # Set the range from the furthest left to i

                if i+1 in lRanges: # If there is a number to the right
                    nr = lRanges[i+1] # Get the furthest right from that number
                    lRanges.pop(i+1) # Remove the range from the number to the right
                    lRanges[l] = nr # Add the range from the furthest left
                    rRanges[nr] = l # Set the range from the furthest right to the furthest left 
                

            # If i isn't in a bound in a range
            # (and hasn't been seen as previously checked)
            elif (i not in lRanges) and (i not in rRanges):
                # Set i as it's own range that can be expanded upon    
                lRanges[i] = i
                rRanges[i] = i

        longest = 0 # Stores the size of the longest range

        # For each range
        for (key, value) in lRanges.items():
            # Update longest if it's the longest
            if value - key + 1 > longest:
                longest = value - key + 1

        return longest
