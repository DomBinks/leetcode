class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        n = num # Copy num so it can be modified
        rev1 = 0 # Stores num reversed without leading 0s

        # While there are digits to extract from n going from right to left
        while n > 0:
            rev1 *= 10 # Multiply by 10 to make room for the next digit
            rev1 += (n % 10) # Add the next digit
            n //= 10 # Remove the digit from n

        rev2 = 0 # Stores rev1 reversed without leading 0s

        # While there are digits to extract from rev1 going from right to left
        while rev1 > 0:
            rev2 *= 10 # Multiply by 10 to make room for the next digit
            rev2 += (rev1 % 10) # Add the next digit
            rev1 //= 10 # Remove the digit from rev1

        return rev2 == num
