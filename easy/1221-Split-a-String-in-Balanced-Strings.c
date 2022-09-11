// Returns the maximum number of balanced strings that can be obatined
int balancedStringSplit(char *s){
    int out = 0; // Tracks the current number of balanced strings
    char *pointer = s; // Pointer to the current character
    int ls = 0; // Tracks the number of 'L's in the current substring
    int rs = 0; // Tracks the number of 'R's in the current substring

    while(*pointer != '\0') // While the pointer is on the string
    {
        if(*pointer == 'L')
        {
            ls++;
        }
        if(*pointer == 'R')
        {
            rs++;
        }

        if(ls == rs) // If the current substring is balanced
        {
            out++; // Increment the output
            ls = 0; // Reset the values
            rs = 0;

        }

        pointer++; // Move the pointer to the next character
    }

    return out;
}