class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = 0;
        vector<bool> out;

        // Find the max value in the input vector
        for(int i = 0; i < candies.size(); i++)
        {
            if(candies[i] > max)
                max = candies[i];
        }

        // Check each value to see if it's bigger with the extra candies
        for(int i = 0; i < candies.size(); i++)
        {
            if(candies[i] + extraCandies >= max)
                out.push_back(true);
            else
                out.push_back(false);
        }

        return out;
    }
};
