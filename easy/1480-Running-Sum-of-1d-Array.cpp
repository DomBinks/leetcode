class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sum; // Contains the running total
        int length = nums.size(); // Size of the input and output vectors
        sum.push_back(nums[0]); // Adds the first element to the out vector
        for(int i = 1; i < length; i++) // For each element in the in vector
        {
            // Add the element to the running total
            sum.push_back(sum.back() + nums[i]);
        }
        
        return sum;
    }
};
