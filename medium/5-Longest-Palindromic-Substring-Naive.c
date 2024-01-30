#include <string.h>
#include <stdlib.h>

// Returns the longest palindromic substring
char *longestPalindrome(char *s){
    int sLength = strlen(s);
    char *longest = calloc(1, sizeof(char)); // Stores the return string
    longest[0] = '\0'; // Sets the current substring to ""
    int longestLength = 0;

    // If the input string is empty
    if(strcmp(s,"") == 0)
    {
        return longest;
    }

    // If the input string contains 1 character
    if(sLength = 1)
    {
        free(longest);
        longest = calloc(2, sizeof(char));
        longest[0] = s[0];
        longest[1] = '\0';
    }

    // Track where we are in the input string
    char *start = s;
    char *finish = start+strlen(s)-1;

    // For each character in the input string
    while(start < finish && start + (longestLength / 2) < finish)
    {
        // Used to approach start from the last character
        char *end = finish;

        // White the end pointer hasn't past the front character
        while(end > start && end - s > longestLength)
        {
            // If a matching pair of characters has been found
            if(*start == *end)
            {
                // Used to go through the current substring
                char *front = start;
                char *back = end;

                // Move through the characters in the substring
                while(*front == *back && front < back)
                {
                    front++;
                    back--;
                }

                // If the substring is a palindrome
                if(front == back || front-1 == back)
                {
                    // If it is the biggest seen so far
                    if(end-start+1 > longestLength)
                    {
                        longestLength = end-start+1;
                        free(longest);
                        longest = calloc(longestLength+1,sizeof(char));
                        longest[longestLength] = '\0';
                        for(int i = 0; i < longestLength; i++)
                        {
                            longest[i] = *(start+i);
                        }
                    }
                }
            }
        
            end--;
        }

        start++;
    }

    return longest;
}