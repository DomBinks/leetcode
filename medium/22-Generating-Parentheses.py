class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = {} # Stores the combinations for each n
        brackets[0] = [] # No combinations for 0 pairs
        brackets[1] = ["()"] # Only combination for 1 pair

        # For each combination from 2 to n (including)
        for i in range(2, n+1):
            brackets[i] = [] # Create list to store combinations

            # Add all combinations made by enclosing the previous size
            # combinations in brackets
            for c in brackets[i-1]:
                brackets[i].append("(" + c + ")")

            # Add all combinations made by using all the combinations
            # of previous sizes that sum to i
            for j in range(1, i): # For each possible side to combine with
                for p in brackets[j]: # Get the brackets for this size
                    for q in brackets[i-j]: # Get the complementing brackets
                        brackets[i].append(p+q) # Add the combination to the list
            
            # Turn the list to a dictionary and then the keys back into a list
            # in order to remove any duplicate combinations
            brackets[i] = list(dict.fromkeys(brackets[i]))

        return brackets[n]
