class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 # Lower bound
        up = len(nums) - 1 # Upper bound

        # While the range is valid
        while low <= up:
            # Get the midpoint of the range
            mid = low + ((up - low) // 2)

            # Check the midpoint of the range
            if(nums[mid] == target):
                return mid
            # If midpoint is higher
            elif nums[mid] > target:
                # Move upper down
                up = mid - 1
            # If midpoint is lower
            else:
                # Move loewr up
                low = mid + 1

        return -1
