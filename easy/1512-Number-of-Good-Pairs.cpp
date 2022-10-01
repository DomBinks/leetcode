class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int out = 0; // Number of good pairs

        // For each pair where i < j
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = i+1; j < nums.size(); j++)
            {
                if(nums[i] == nums[j] && i < j) 
                {
                    out++; // Increment out if it's a good pair
                }
            }
        }
        
        return out;
    }
};
