class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ") # Get the words from the sentence

        length = {} # Maps lengths to words of that length

        # For each word
        for word in words:
            # Add that word to the map
            if len(word) not in length:
                length[len(word)] = [word.lower()]
            else:
                length[len(word)].append(word.lower())

        arr = list(length.items()) # Get the list of map entries
        arr.sort() # Sort the entries by the length of their words

        # Set the 1st character of the 1st word in the list of the
        # 1st length to be capitalised
        arr[0][1][0] = arr[0][1][0][0].upper() + arr[0][1][0][1:]

        out = "" # Stores the output string

        # For each length and words pair in the list
        for pair in arr:
            # For each word in the words list
            for word in pair[1]:
                # Add that word to the output with a space
                out += " "
                out += word

        # Return the output string without the leading space
        return out[1:]
