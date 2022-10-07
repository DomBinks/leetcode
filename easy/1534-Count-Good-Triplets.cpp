class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int out = 0;
        
        // Loop over all valid i, j, k combinations
        for(int i = 0; i < arr.size() - 2; i++)
        {
            for(int j = i+1; j < arr.size() - 1; j++)
            {
                for(int k = j+1; k < arr.size(); k++) 
                {
                    // Check conditions
                    if(abs(arr[i] -arr[j]) <= a && \
                       abs(arr[j] - arr[k]) <= b && \
                       abs(arr[i] - arr[k]) <= c)
                    {
                        // Increment out if the conditions are met
                        out++;
                    }
                }
            }
        }
        
        return out;
    }
};
