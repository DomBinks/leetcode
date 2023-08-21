class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Convert strings to lists of word strings
        words = s1.split(" ") + s2.split(" ")

        m = {} # Stores the number of occurences of each word

        # For each word in the list
        for word in words:
            # If it hasn't been seen
            if word not in m:
                m[word] = 1 # Set it's occurrences to 1
            else:
                m[word] += 1 # Increment the occurrences

        # Return the list of words where the number of occurrences is equal to 1
        return [word for (word, occurrences) in m.items() if occurrences == 1]
