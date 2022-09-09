class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        """Returns the decoded version of the encoded message"""
        map = {' ': ' '} # Maps letters to their decoded version
        letters = "abcdefghijklmnopqrstuvwxyz"
        counter = 0 # Keeps track of the current letter 
        for char in key: # For each character in the key string
            if char not in map: # If the letter doesn't have a mapping
                map[char] = letters[counter] # Adds the mapping to map
                counter += 1 # Moves to the next letter

        out = "" # Decoded string
        for char in message:
            out += map[char] # Append the decoded character to out

        return out