class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) // No strings case
            return "";

        vector<char> prefix; // Stores the prefix

        int counter = 0; // Tracks the index of the current character
        while(true)
        {
             // If counter is past the last character of the first string
            if(counter >= strs[0].length())
                return string(prefix.data(), prefix.size());

            // Sets the current character to the character in the first string
            // at the index counter
            char current = strs[0][counter];
            // For the rest of the strings
            for(int i = 1; i < strs.size(); i++)
            {
                // If the counter is past the last character of the string
                // or is different to the current character
                if(counter >= strs[i].length() || current != strs[i][counter])
                    return string(prefix.data(), prefix.size());
            }

            // If the current character is in all the strings add it to prefix
            prefix.push_back(current);
            counter++; // Increment the counter to look at the next character
        }

        return string(prefix.data(), prefix.size());
    }
};
