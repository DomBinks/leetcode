class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Returns if the string is a valid palindrome"""

        # New string with only alphanumeric characters
        newString = ""

        # Put all the alphanumeric characters in the new string
        for i in range(len(s)):
            if(s[i].isalnum()):
                newString += s[i]

        # Make all the letters lowercase
        newString = newString.lower()

        # Pointers to the front and back of the string
        front = 0
        back = len(newString) - 1

        # While the pointers haven't passed each other
        while(front < back):
            # Compare the characters at either end
            if(newString[front] != newString[back]):
                return False
            else:
                front += 1
                back -= 1

        return True