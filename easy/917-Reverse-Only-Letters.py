class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [] # Stores all the letters seen

        # For each character in s
        for i in range(0, len(s)):
            # If the character is a letter
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z'):
                letters.append(s[i]) # Add it to the liist of letters

        out = "" # Stores the output string

        # For each character in s
        for c in s:
            # If the character is a letter
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                out += letters[-1] # Append the last letter in the list to out
                letters.pop(-1) # Remove the last letter in the list
            # If the character isn't a letter
            else:
                out += c # Append the character to out

        return out
