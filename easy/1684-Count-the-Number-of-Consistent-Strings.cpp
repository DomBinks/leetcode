class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int out = 0; // Store number of consistent strings
        
        int letters[26]; // Store letters that are in allowed
        // Initialise letters to 0s
        for(int i = 0; i < 26; i++)
            letters[i] = 0;
        // Set letters index to 1 if the letter is in allowed
        for(int i = 0; i < allowed.length(); i++)
            letters[allowed[i] - 97] = 1;
        
        // For each word
        for(int i = 0; i < words.size(); i++)
        {
            bool consistent = true; // Track if current word is consistent
            // For each character in a word
            for(int j = 0; j < words[i].length(); j++) 
            {
                // If the character isn't in allowed
                if(letters[words[i][j] - 97] == 0)
                {
                    consistent = false;
                    break;
                }
            }
            
            // If the current word is consistent
            if(consistent)
                out++;
        }
        
        return out;
    }
};
