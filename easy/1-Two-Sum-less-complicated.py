from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j and (nums[i] + nums[j] == target) or (target == 0 and nums[i] == 0 and nums[j] == 0)):
                    return [i, j] 

print(Solution.twoSum(None, [0,3,-3,4,-1], -1))