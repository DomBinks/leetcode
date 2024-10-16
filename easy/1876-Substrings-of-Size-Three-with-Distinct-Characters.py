class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # Check length is >= 3
        if len(s) < 3:
            return 0

        total = 0 
        # For each substring length 3
        for i in range(2,len(s)):
            # If any of the characters are the same
            if s[i] == s[i-1] or s[i] == s[i-2] or s[i-1] == s[i-2]:
                # Don't increment the counter
                continue
            # If none of the characters are the same
            else:
                # Increment the counter
                total += 1

        return total
