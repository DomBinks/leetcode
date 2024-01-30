class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        best = 0 # Max consecutive 1s
        back = 0 # Back index of subarry
        front = 0 # Front index of subarray

        size = 0 # Current size of subarray
        # While the back of the array hasn't been reached
        while front != len(nums):
            # If there is a 1
            if nums[front] == 1:
                # Move the front index forward
                front += 1
                size += 1
                # Update the size if needed
                if size > best:
                    best = size
            
            # If there is a 0 and there are flips left
            elif k > 0:
                # Use a flip
                k -= 1
                # Move the front index forward
                front += 1
                size += 1
                # Update the size if needed
                if size > best:
                    best = size

            # If there are no flips left
            else:
                # Keep moving the back index up until a flip is reclaimed
                while k == 0:
                    size -= 1
                    if nums[back] == 0:
                        k += 1
                    back += 1

        return best
