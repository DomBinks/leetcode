class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int out = 0;
        // Store whether an ASCII value is a jewel
        bool jewelStones[123];
        // Init the array
        for(int i = 0; i < 123; i++)
            jewelStones[i] = false;
        
        // Set the indices of ASCII values that are jewels to true
        for(int i = 0; i < jewels.length(); i++)
        {
            jewelStones[jewels[i]] = true;
        }
        
        // Check each stone to see if it is a jewel
        for(int i = 0; i < stones.length(); i++)
        {
            if(jewelStones[stones[i]]) 
                out++;
        }
        
        return out;
    }
};
