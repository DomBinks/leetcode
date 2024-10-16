class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        sortedS = sorted(s) # s but sorted

        length = -1 # Length of each section of the same character
        char = sortedS[0] # The character in the current section
        current = 1 # The length of the current section

        # For each character in sortedS
        for i in range(1, len(sortedS)):
            # If this character is still in this section
            if sortedS[i] == char:
                current += 1 # Increment the length of the current section

            # If this character isn't in this section i.e. new section
            else:
                # If the section length hasn't been defined
                # i.e. this is the first section
                if length == -1:
                    length = current # Define the length of each section

                # If the section length has been defined
                else:
                    # If this secton doesn't match the length each section
                    # should be
                    if current != length:
                        return False

                char = sortedS[i] # Update the character in the current section
                current = 1 # Set the length of the current section to just this character

        # Return whether the last section matches the length each section should be
        # or the string is 1 big section
        return current == length or length == -1
