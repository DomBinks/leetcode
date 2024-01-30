class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        arr = [False] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, nums[i]):
                if i+j < len(arr):
                    arr[i+j] = True

        a = True
        for b in arr:
            a = a and b

        return a
