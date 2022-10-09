class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ') # Split string into words
        ordered = [""] * 10 
        out = ""
        
        for word in words:
            # Store the word in the index of the end number
            ordered[int(word[-1])] = word[0:len(word)-1] 
            
        # use strip() to remove whitespace at front and back
        return " ".join(ordered).strip()
