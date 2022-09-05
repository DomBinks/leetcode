#include <string.h>

// Return the length of the longest substring with no repeated characters
int lengthOfLongestSubstring(char *s)
{
    int length = strlen(s); // Length of the string
    int longest = 0; // Current longest substring

    for(int i = 0; i < length; i++) // For each letter
    {
        int occurrences[128] = {0}; // Number of occurrences of each letter
        int currentLength = 0; // Current substring length

        for(int j = i; j < length; j++) // For each letter after i
        {
            if(occurrences[s[j]] > 0) // If the current letter has already appeared
            {
                break;
            }
            else
            {
                occurrences[s[j]]++; // Increment the occurrences of the current letter
                currentLength++; // Increment the current substring length
            }
        }

        if(currentLength > longest) // If the current substring is the longest
        {
            longest = currentLength; // Update the longest value

            // If the length of the rest of the string to look at is
            // shorter than the current longest substring
            if(length - i < longest)
            {
                break;
            }
        }
    }

    return longest;
}