class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            
            elif t[i] in map.values():
                return False

            else:
                map[s[i]] = t[i]

        return True