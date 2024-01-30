class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = [] # Duplicate sequences
        seen = {} # Keep track of seen sequences

        # If the sequence is less than 10
        if len(s) < 10:
            return sequences

        # For each substring of size 10
        for i in range(10, len(s) + 1):
            # If the substring hasn't been seen
            if s[i-10:i] not in seen:
                # Add it to the map
                seen[s[i-10:i]] = 1

            # If the map indicates that it's only been seen once
            elif seen[s[i-10:i]] == 1:
                # Add it to the list of duplicate sequences
                sequences.append(s[i-10:i])
                # Update the map
                seen[s[i-10:i]] += 1

        return sequences
