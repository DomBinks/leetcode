class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int) # Create a dictionary to count the seen words
        chars = 0 # Counts the characters in the longest palindrome
        mids = 0 # Counts the number of words that could be placed in the middle

        # For each word
        for word in words:
            # Get the reverse of the word
            rev = word[1] + word[0]

            # If the word could be placed in the middle
            if word[0] == word[1]:
                mids += 1

            # If the reverse has been seen so we can make a pair
            if seen[rev] > 0:
                seen[rev] -= 1 # Decrement the number of the reverse available
                chars += 4 # Increment the count by 4 for the size of the 2 words

                # If these words were added to the amount that could be in the middle
                if word[0] == word[1]:
                    mids -= 2 # Decrement for both of the words used in this pair

            # If the reverse hasn't been seen
            else:
                # Increment the number of times this word has been seen
                seen[word] += 1

        # If there is a word that can be placed in the middle
        if mids > 0:
            chars += 2 # Increment the count by 2 for the middle word

        return chars

