class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Returns whether the input number is a palindrome"""
        string = str(x) # Store the number as a string
        mid = len(string) // 2 # Find the mid point
        if len(string) % 2 != 0: # Set front and back pointers
            front = mid - 1
            back = mid + 1 # Skip the middle element if odd length
        else:
            front = mid - 1
            back = mid # Middle element is back if even length

        for i in range(mid): # For half the length
            if string[front] != string[back]: # If the nums are diff
                return False
            
            front -= 1 # Move pointers
            back += 1

        return True