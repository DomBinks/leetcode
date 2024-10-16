class Solution {
public:
    int largestInteger(int num) {
        vector<int> digits; // Store the digits in reverse order
        priority_queue<int> evens; // Store the even digits in descending order
        priority_queue<int> odds; // Store the odd digits in descending order

        int x = num; // Used to get each digit
        while(x > 0)
        {
            int digit = x % 10; // Get the right-most digit
            digits.push_back(digit); // Add it to the vector of digits
            x /= 10; // Go to the next digit

            if(digit % 2 == 0) // If the digit is even
            {
                evens.push(digit); // Add to evens
            }
            else // If the digit is odd
            {
                odds.push(digit); // Add to odds
            }
        }

        int out = 0; // Output number
        vector<int>::reverse_iterator it = digits.rbegin(); // Left-most digit

        // For each digit left to right
        while(it != digits.rend())
        {
            out *= 10; // Move the previous digit left 1 column
            if(*it % 2 == 0) // If the digit in the original number is even
            {
                x = evens.top(); // Add the highest even number to the output
                evens.pop(); // Remove that even number from evens
            }
            else // If the digit in the original number is odd
            {
                x = odds.top(); // Add the highest odd number to the output
                odds.pop(); // Remove that odd number from odds
            }
            out += x; // Add the number to the output
            it++; // Get the next digit in the original number
        }

        return out;
    }
};
