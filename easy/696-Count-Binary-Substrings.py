class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0 # Total substrings seen
        prev = 0 # 0s or 1s in last section
        count = 0 # 0s or 1s in current section
        current = s[0] # Whether current section is 0s or 1s

        # For each character
        for i in range(0, len(s)):
            # If still in the same section
            if s[i] == current:
                count += 1 # Increment section count

                # If there are previous digits to pair up with
                if prev > 0:
                    total += 1 # Increment the substrings seen
                    prev -= 1 # Decrement the digits remaining to pair up with

            # If the section has changed digit
            else:
                # Set the previous section to the current section, -1 for pairing with this character
                prev = count - 1 
                count = 1 # Set this section's size to 1 as it contains this character
                total += 1 # Set Increment the substrings seen as this switch is one
                current = s[i] # Update the current digit

        return total
