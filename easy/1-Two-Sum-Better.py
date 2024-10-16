from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Returns an array containing the indices of the 2 numbers
           in nums that sum to give the target number"""

        # Hashmap to store the indices of seen values
        # Key: value seen, Value: index of the value
        map = {}  
        for i in range(len(nums)):
            # If the number we need has been seen
            if target - nums[i] in map:
                # Return i and the index of the number we need
                return [i, map[target-nums[i]]]
            # Otherwise add current value to map
            else:
                map[nums[i]] = i