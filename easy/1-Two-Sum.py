from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        nums.reverse()

        for i in nums:
            if(i > target):
                nums.remove(i)

        while True:
            first = nums.pop(0)
            current = first 
            targetNums = [first]
            for i in nums:
                if current + i < target:
                    targetNums.append(i)
                    current += i 
                if current + i == target:
                    targetNums.append(i)
                    return targetNums

print(Solution.twoSum(None, [11,7,15,2], 9))