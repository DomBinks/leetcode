class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int X = 0; // Stores X value

        // For each operation in operations
        for(auto operation = operations.begin(); operation != operations.end(); operation++)
        {
            bool sign; // true - increment X, false - decrement X
            int index;
            // Find out which index of the string contains the sign
            if((*operation)[0] == 'X') // If first letter is 'X'
                index = 2; // Index 2 contains the sign
            else // If the first letter is a sign
                index = 0; // Index 0 contains the sign

            if((*operation)[index] == '+') // If the sign is '+'
                sign = true;
            else // If the sign is '-'
                sign = false;

            if(sign) // Increment if sign is true
                X++;
            else // Decrement if sign is false
                X--;
        }

        return X;
    }
};
