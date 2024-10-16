class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Map of characters in string s to characters in string t
        map = {}
        
        # For all characters
        for i in range(len(s)):
            # If the character in s already has a mapping
            if s[i] in map:
                # If the mapping doesn't map to the value in t
                if map[s[i]] != t[i]:
                    return False
            
            # If the character in t already has a mapping to it
            elif t[i] in map.values():
                return False

            else:
                # Add the mapping from the character in s to the character in t
                map[s[i]] = t[i]

        return True