class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sorted; // nums but sorted
        for(vector<int>::iterator i = nums.begin(); i != nums.end(); i++)
        {
            sorted.push_back(*i);
        }
        sort(sorted.begin(), sorted.end());
        
        // Map value to number of values below it 
        map<int, int> sortedMap;
        
        // Track numbers already seen so we know when not to update sortedMap
        bool seen[502];
        for(int i = 0; i < 502; i++)
            seen[i] = false;
        
        // For each value in the sorted array
        for(int i = 0; i < sorted.size(); i++)
        {
            // If the value hasn't been seen yet
            if(seen[*(sorted.begin()+i)] == false)
            {
                seen[*(sorted.begin()+i)] = true; // Set as seen
                
                // Map to numbers of values below it
                // (number of values before it as array is sorted)
                sortedMap[*(sorted.begin()+i)] = i;
            }
        }
                    
        // Go through original nums array and create a new array
        // where each index is the mapping to the number of values below it 
        vector<int> out; 
        for(int i = 0; i < nums.size(); i++)
        {
            out.push_back(sortedMap[nums[i]]);                
        }
        
        return out;
    }
};
