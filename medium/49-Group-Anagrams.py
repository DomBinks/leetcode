class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Stores each word in an array of words, indexed by the string of
        # the letters in the word sorted
        anagrams = {}

        # For each word in the input
        for w in strs:
            # Get that word's letters sorted
            s = str(sorted(w))

            # If that string of the letters in the word sorted is a valid key
            if s in anagrams:
                # Append to the existing array
                anagrams[s].append(w)

            # If it's not a valid key
            else:
                # Add the word to a new array at the index of the string of
                # letters in the word sorted
                anagrams[s] = [w]

        out = [] # Stores the output array

        # For each array in the map
        for l in anagrams.values():
            out.append(l) # Add it to the output array

        return out
