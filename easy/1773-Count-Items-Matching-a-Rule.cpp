class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int out = 0;
        // Stores the index of the item element array to compare to ruleValue
        int ruleKeyNum;
         
        // Convert the ruleKey to the correct array index
        if(ruleKey == "type")
            ruleKeyNum = 0;
        else if(ruleKey == "color")
            ruleKeyNum = 1;
        else
            ruleKeyNum = 2;
        
        // Check each item element array value
        for(int i = 0; i < items.size(); i++)
            if(items[i][ruleKeyNum] == ruleValue)
                out++;
        
        return out;
    }
};
