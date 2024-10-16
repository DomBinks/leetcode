class Solution {
public:
    int subtractProductAndSum(int n) {
        // Convert n to a string so we can access
        // the individual digits
        string nString = to_string(n);
        
        // To store the product and sum
        int product = 1;
        int sum = 0;
        
        // For each digit
        for(int i = 0; i < nString.length(); i++)
        {
            // Convert the digit from a character to an int
            // by substracting '0' (48)
            int digit = nString[i] - '0';
            
            // Update the product and sum variables
            product *= digit;
            sum += digit;
        }
        
        return product - sum;
    }
};
