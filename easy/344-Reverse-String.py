class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # Store a copy of s in sCopy
        sCopy = [] 
        for i in s:
            sCopy.append(i)
        
        # Cache the value of len(s)
        length = len(s)

        # Replace each value in s with the value at the same index
        # coming from the opposite direction
        for i in range(length):
            s[i] = sCopy[length-1-i]