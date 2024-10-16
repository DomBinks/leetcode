class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        int out = 0;
        
        // Loop over each possible value of i
        // (all but the last 2 values as j and k have to be bigger)
        for(int i = 0; i < nums.size() - 2; i++)     
        {
            // See if there is a nums[j] that satisfies nums[j] == diff + nums[i]
            vector<int>::iterator j = find(nums.begin()+i, nums.end(), diff+nums[i]);
            // If there is a nums[j] that satisfies the equation and 
            // there is a nums[k] that satisfies nums[k] = 2 * diff + nums[i] 
            if(j != nums.end() && find(j, nums.end(), 2 * diff + nums[i]) != nums.end())
                out++;
        }
        
        return out;
    }
};
