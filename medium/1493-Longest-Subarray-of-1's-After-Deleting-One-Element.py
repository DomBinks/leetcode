class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0 # Track the longest subarray
        back = 0 # Back index of the current subarray
        removed = -1 # Index of the removed 0

        # Keep expanding the subarray forwards
        for front in range(0,len(nums)):
            # If a 0 hasn't been removed yet
            if nums[front] == 0 and removed < 0:
                removed = front # Set the index of the 0
            # If there is a 0 in the subarray
            elif nums[front] == 0 and removed >= 0:
                # -1 as implicitly deals with front being an extra
                # index ahead (at the next 0) but doesn't deal with
                # removing the 0 from the overall length as required
                longest = max(longest, front - back - 1)

                # +1 as removed is the index of the 0
                back = removed + 1
                removed = front # Set the index of the 0

        longest = max(longest, front - back)

        return longest
