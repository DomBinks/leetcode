class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> output; // Stores the output array
        vector<int>::iterator xs = nums.begin(); // Pointer to the 1st half
        vector<int>::iterator ys = nums.begin() + n; // Pointer to the 2nd half
        
        // Loop over all the elements
        while(xs != nums.begin() + n || ys != nums.end())
        {
            if(xs != nums.begin() + n) // If there is an element in the 1st half
            {
                output.push_back(*xs); // Add it to the end of the output
                xs++; // Increment the pointer
            }
            if(ys != nums.end()) // If there is an element in the 2nd half
            {
                output.push_back(*ys); // Add it to the end of the output
                ys++; // Increment the pointer
            }
        }
        
        return output; // Return the output vector
    }
};
