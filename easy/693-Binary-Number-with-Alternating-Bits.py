class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        for i in range(0, len(bin(n)) - 1):
            if bin(n)[i] == bin(n)[i+1]:
                return False

        return True
