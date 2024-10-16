class Solution {
public:
    string defangIPaddr(string address) {
        int sLen = address.length(); // Length of the input string
        // Create an output string with 6 extra spaces for the brackets
        string out(sLen+6, ' ');
        
        // i - index in address, j - index in out
        for(int i = 0, j = 0; i < sLen; i++)
        {
            if(address[i] == '.')
            {
                out[j++] = '[';
                out[j++] = address[i];
                out[j++] = ']';
            }
            else
            {
                out[j++] = address[i];
            } 
        }
        
        return out;
    }
};
