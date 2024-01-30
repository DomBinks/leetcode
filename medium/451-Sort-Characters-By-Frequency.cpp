class Solution {
public:
    string frequencySort(string s) {
        map<char, int> freq; // Store the frequency of each letter

        // Iterate through each character
        string::iterator it = s.begin();
        while(it != s.end())
        {
            // Update the map with that character
            if(freq.find(*it) == freq.end())
            {
                freq[*it] = 1;
            }
            else
            {
                freq[*it]++;
            }

            it++;
        }

        // Stores the characters sorted by their frequency
        priority_queue<pair<int, char>> sorted;
        for(pair<char, int> x : freq)
        {
            sorted.push(make_pair(x.second, x.first));
        }

        string out = ""; // Stores the output string

        // While there characters left to add
        while(!sorted.empty())
        {
            // Get the character with the highest frequency not added
            pair<int, char> y = sorted.top();
            sorted.pop();

            // Add that character to the output based upon it's frequency
            for(int i = 0; i < y.first; i++)
            {
                out.push_back(y.second);
            }
        }

        return out;
    }
};
