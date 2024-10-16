from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Add 1 to the input number provided as a list"""
        digits[-1] += 1 # Adds 1 to the last digit

        # Loop back through each digit but the first
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] > 9: # If there is a carry
                digits[i] -= 10 # Remove the carry from this digit
                digits[i-1] += 1 # Move the carry to the next digit
        
        if digits[0] > 9: # If there is a carry for the first digit
            digits[0] -= 10 # Remove the carry from this digit
            digits = [1] + digits # Add [1] to the front of the list

        return digits