class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 # Longest substring seen so far
        low = 0 # Earliest index of a character in the current window

        current = set() # Contains the characters in the current window

        # For each character in the string
        for i in range(0, len(s)):
            # If this character isn't in the current window
            if s[i] not in current:
                # Add to the set
                current.add(s[i]) 
            # If this character is in the window
            else:
                # Update the longest if this set is the longest
                # so far
                if i - low > longest:
                    longest = i - low

                # Keep removing characters from the left until you
                # remove the character at index i (now a duplicate)
                while s[i] in current:
                    current.remove(s[low])
                    low += 1

                # Re-add the character at index i
                current.add(s[i])

        # Check if the final window is the longest
        if len(current) > longest:
            longest = len(current)

        return longest
