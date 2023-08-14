class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # How many times letters have been seen in s
        lettersS = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,
        'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,
        't': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
        
        # How many times letters have been seen in t
        lettersT = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,
        'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,
        't': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}

        # Count the letters in s
        for c in s:
            lettersS[c] += 1

        # Count the letters in t
        for c in t:
            lettersT[c] += 1

        # For each letter
        for (key, value) in lettersS.items():
            # If the number of each letter s and t is different
            if value != lettersT[key]:
                return False

        # If s and t have the same amount of each letter
        return True

