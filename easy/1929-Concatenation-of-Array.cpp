class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        // Define new array with double the length
        vector<int> ans(2*nums.size());
        for(int i = 0; i < nums.size(); i++)
        {
            // Copy value to:
            ans[i] = nums[i]; // Original location
            ans[i+nums.size()] = nums[i]; // Original location + offset
        }
        
        return ans;
    }
};
