class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans(nums.size()); // Initialise ans array
        
        // Loop over each index in nums/ans
        for(int i = 0; i < nums.size(); i++)
        {
            // Use the rule to work out the value for ans
            ans[i] = nums[nums[i]];
        }
        
        return ans;
    }
};
