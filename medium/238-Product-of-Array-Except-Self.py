class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums) # Stores the product of the elements up to and including this index
        suffix = [1] * len(nums) # Stores the product of the elements from this index to the end

        prefix[0] = nums[0] # Set the first prefix to just the first element
        suffix[len(nums)-1] = nums[len(nums)-1] # The the last suffix to just the last element

        # For each index between the first and last
        for i in range(1, len(nums)):
            # Set the prefix at this index as the previous prefix times the number at this index
            prefix[i] = prefix[i-1] * nums[i]
            # Set the suffix at this index as the suffix of the next number times the number at this index
            suffix[len(nums)-1-i] = suffix[len(nums)-i] * nums[len(nums)-1-i]

        out = [1] * len(nums)
        # Set the product except the first element to the suffix of the second element
        out[0] = suffix[1]
        # Set the product except the last element to the prefix of the penultimate element
        out[len(nums)-1] = prefix[len(nums)-2]

        # For each index between the first and last
        for i in range(1, len(nums)-1):
            out[i] *= prefix[i-1] # Multiply by the product of all the previous elements
            out[i] *= suffix[i+1] # Multiply by the product of all the next elements

        return out
