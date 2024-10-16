class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)

        total = original
        while total in s:
            total *= 2

        return total
