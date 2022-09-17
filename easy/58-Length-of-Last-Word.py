class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """Return the length of the last word in the string"""
        index = len(s) - 1 # Final index
        while s[index] == ' ': # Skip over any trailling whitespace
            index -= 1
        
        back = index # Index of the last character of the last work

        # Loop over all the characters in the last word
        while s[index] != ' ' and index >= 0:
            index -= 1

        return back - index # Return the difference of the back and front
