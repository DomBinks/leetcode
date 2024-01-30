class Solution {
public:
    vector<int> findOriginalArray(vector<int>& changed) {
        if(changed.size() % 2 != 0) // Can't be an odd length array
            return vector<int>();

        sort(changed.begin(), changed.end());
        vector<int> output;

        int loops = changed.size() / 2; // Loop over half of the array
        for(int i = 0; i < loops; i ++) // i.e. all the doubled values
        {
            int current = changed[0]; // Pop the value from the front of the array
            changed.erase(changed.begin());

            // Looked for the doubled value
            if(binary_search(changed.begin(), changed.end(), current*2))
            {
                // Find the index of the doubled value
                auto indexIt = find(changed.begin(), changed.end(), current*2);
                int index = indexIt - changed.begin();

                // Remove the doubled value
                changed.erase(changed.begin()+index);
                output.push_back(current); // Add the original value to output
            }
            // Return empty if there isn't the doubled value
            else
                return vector<int>();
        }

        return output;
    }
};
