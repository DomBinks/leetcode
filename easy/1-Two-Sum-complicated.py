from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCopy = nums.copy()
        numsCopy2 = nums.copy()
        nums.sort()
        for i in nums:
            if i > 0:
                nums.reverse()
                break

        while True:
            print(nums)
            first = nums.pop(0)
            current = first 
            targetNums = [first]

            if current == target and current != 0:
                continue

            for i in nums:
                if target >= 0:
                    if current + i <= target:
                        targetNums.append(i)
                        current += i 
                else:
                    if current + i >= target:
                        targetNums.append(i)
                        current += i 

            if current == target:
                break

        returnList = []
        while targetNums != []:
            elem = targetNums.pop(0)
            returnList.append(numsCopy.index(elem))
            numsCopy[numsCopy.index(elem)] = None

        returnList.sort()
        return returnList
        
print(Solution.twoSum(None,[0,3,-3,4,-1], -1))