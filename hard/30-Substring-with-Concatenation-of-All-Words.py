class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = [] # Indices of concatenated substrings
        wordLen = len(words[0]) # Length of each word
        concatLen = wordLen * len(words) # Length of each substring

        # If the string s isn't big enough for a substring
        if len(s) < concatLen:
            return []

        # Sort the list of words to check for
        sortedWords = sorted(words)
        # For each substring
        for i in range(0, len(s)-concatLen+1):
            # Get the substring
            substring = s[i:i+concatLen]
            # Split it into a list of words
            subWords = []
            for j in range(0, concatLen, wordLen):
                subWords.append(substring[j:j+wordLen])
            
            # If the sorted list of substring words is equal
            # to the sorted list of words
            if sortedWords == sorted(subWords):
                # Add that index to the list
                indices.append(i)

        return indices
