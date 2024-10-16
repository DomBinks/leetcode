#include <stdbool.h>
#include <string.h>

// Returns true if the ransomNote string can be made using individual
// characters from the magazine string, and false if it can't
bool canConstruct(char *ransomNote, char *magazine)
{
    // a = 97, z = 122
    int n[123] = {0};   // Stores occurances of letters in ransomNote 
    int m[123] = {0};   // Stores occurances of letters in magazine 
    int nLength = strlen(ransomNote);
    int mLength = strlen(magazine);

    // Calculates the number of occurances of each letter in
    // ransomNote
    for (int i = 0; i < nLength; i++)
    {
        n[ransomNote[i]]++; 
    }

    // Calculates the number of occurances of each letter in magazine
    for (int i = 0; i < mLength; i++)
    {
        m[magazine[i]]++;
    }

    // Loops over every letter
    for (int i = 97; i < 123; i++)
    {
        // Checks to see if there are more occurances of a letter in
        // ransomNote than in magazine
        if (n[i] > m[i])
        {
            // Returns false if there are as it means ransomNote can't 
            // be recreated using individual letters from magazine
            return false;
        }
    }

    // Returns true if there aren't as it means ransomNote can be
    // recreated using individual letters from magazine
    return true;
}