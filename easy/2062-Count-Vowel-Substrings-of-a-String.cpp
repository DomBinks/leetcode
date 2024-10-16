class Solution {
public:
    bool isVowel(char letter) {
        if(letter == 'a' || letter == 'e' || letter == 'i' ||
           letter == 'o' || letter == 'u')
            return true;
        else
            return false;
    }
    
    int getVowelIndex(char letter) {
        if(letter == 'a')
            return 0;
        if(letter == 'e')
            return 1;
        if(letter == 'i')
            return 2;
        if(letter == 'o')
            return 3;
        if(letter == 'u')
            return 4;
        else
            return -1;
    }
    
    void checkForVowels(string word, int start, int end, int *vowels) {
        vowels[0] = 0; 
        vowels[1] = 0; 
        vowels[2] = 0; 
        vowels[3] = 0; 
        vowels[4] = 0; 
        
        for(int i = start; i <= end; i++)
        {
            if(isVowel(word[i])) 
                vowels[getVowelIndex(word[i])]++;
        }
    }
    
    int countVowelSubstrings(string word) {
        int out = 0;
        int vowels[5] = {0, 0, 0, 0, 0};
        
        if(word.length() < 5)
            return out;
       
        int front = 0;
        int back = 4;
        while(out < 1 && back < word.length())
        {
            checkForVowels(word, front, back, vowels);
            if(vowels[0] && vowels[1] && vowels[2] && vowels[3] && vowels[4])
                out++;
            else
            {
                front++;
                back++;
            }
            cout << "a" << endl;
        }
        
        back++;
        while(front <= word.length() - 5 && back < word.length())
        {
            cout << front << " " << back << endl;
            if(isVowel(word[back]))
            {
                vowels[getVowelIndex(word[back])]++;
                out++;
                back++;
            }
            else
            {
                if(word.length() - back - 1 < 5) 
                    break;
                else
                {
                    front = back + 1;
                    back = front + 4;
                    checkForVowels(word, front, back, vowels); 
                }
            }
            
        }
        
        return out;
    }
};
