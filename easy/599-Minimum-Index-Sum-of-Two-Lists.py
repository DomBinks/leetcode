class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Stores the index where words are seen in list1
        seen = {}

        # For each word in list1
        for i in range(0, len(list1)):
            # Add the index to the map
            seen[list1[i]] = i

        s = 99999 # Stores the minimum index sum
        l = [] # Stores the words with the minimum index sum

        # For each word in list2
        for i in range(0, len(list2)):
            # If the word is in list1
            if list2[i] in seen:
                # If the index sum is smaller than the current
                if i + seen[list2[i]] < s:
                    # Update the minimum index sum 
                    s = i + seen[list2[i]]
                    # Set the words with this sum to this word
                    l = [list2[i]]

                # If the index sum is equal to the current
                elif i + seen[list2[i]] == s:
                    # Add this word to the list of words
                    l.append(list2[i])

        return l
