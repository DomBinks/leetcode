class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        """Returns the maximum number of words in a sentence in sentences."""

        maximum = 0 # Stores the max value
        for sentence in sentences:
            words = sentence.split(" ") # Split the sentence into words
            if len(words) > maximum: # Check the length
                maximum = len(words) # Update if longer
                
        return maximum
