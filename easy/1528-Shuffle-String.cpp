class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        int length = indices.size(); // Store size of input/output
        string output(length, ' '); // String to store the output in

        for(int i = 0; i < length; i++) // For each input character
        {
            // Index the output string with the value from indices
            // and insert the value from s
            output[indices[i]] = s[i];
        }

        return output;
    }
};
