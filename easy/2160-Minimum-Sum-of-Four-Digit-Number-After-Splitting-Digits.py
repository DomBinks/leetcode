class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num)) # Convert num to an array of number characters
        nums.sort() # Sort the number characters in numerical order
        # The pairs will be the 1st and 3rd element and 2nd and 4th element
        # as that gives the minimum possible values for the 2 numbers.
        # The number characters are then concatenated, converted to integers
        # and summed.
        return int(nums[0]+nums[2]) + int(nums[1]+nums[3]);
