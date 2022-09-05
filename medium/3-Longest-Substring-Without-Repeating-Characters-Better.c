// Return the length of the longest substring with no repeated characters
int lengthOfLongestSubstring(char *s)
{
    int occurrences[128] = {0}; // Number of occurrences of each letter
    int longest = 0; // Current longest substring
    int current = 0; // Current substring length
    char *start = s; // Start substring pointer
    char *end = s; // End substring pointer

    while(*end != '\0') // While there are characters left
    {
        occurrences[*end]++; // Increment occurrences of end letter
        current++; // Increment current substring length

        // While the substring contains duplicate characters
        while(occurrences[*end] > 1)
        {
            occurrences[*start]--; // Decrement occurrences of start letter
            current--; // Decrement current substring length
            start++; // Move start pointer to the next letter
        }

        if(current > longest) // If the current substring is the longest
        {
            longest = current; // Update longest value
        }

        end++; // Move end pointer to the next letter
    }

    return longest;
}