from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Returns an array containing the indices of the 2 numbers
           in nums that sum to give the target number"""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i,j]