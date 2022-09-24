class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) // Special case
            return s;
        
        int length = s.length(); // Store length of input string
        vector<char> output; // Stores the output list of characters
        int offset = (2 * numRows) - 2;
        
        for(int i = 0; i < numRows; i++) // For each row
        {
            // Step to the character on the zigzag
            int firstStep = offset - (2*i);
            // Step to the character on the vertical line
            int secondStep = 2*i;

            // Ensure that characters don't get added to the output twice
            // if there is a step of 0
            if(firstStep == 0)
                firstStep = secondStep;
            if(secondStep == 0)
                secondStep = firstStep;
            
            int index = i; // Keeps track of the current index
            bool toggle = false; // Tracks which step is being added
            while(index < length)
            {
                output.push_back(s[index]); // Add the character to the output
                if(toggle == false) // Add first step to index
                {
                    index += firstStep;
                    toggle = true;
                }
                else // Add second step to index
                {
                    index += secondStep;
                    toggle = false;
                }
            }
        }
        
        return string(output.data(), output.size()); // Convert vector to string
    }
};
