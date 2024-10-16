class Solution {
public:
    int xorOperation(int n, int start) {
        // Define the nums array with the given rule
        vector<int> nums(n); 
        
        for(int i = 0; i < n; i++)
        {
            nums[i] = start + 2 * i;
        }
        
        int out = 0;
        // Loop over every element in nums
        for(int i = 0; i < n; i++)
        {
            // XOR with out
            out = out ^ nums[i];
        }
        
        return out;
    }
};
