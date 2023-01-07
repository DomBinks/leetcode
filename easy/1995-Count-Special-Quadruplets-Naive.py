class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        out = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    for l in range(k+1, len(nums)):
                        if sum == nums[l]:
                            out += 1

        return out