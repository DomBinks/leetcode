class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {} # Contains seen numbers
        for i in nums: # For each number
            if i not in seen: # If not seen
                seen[i] = True # Set as seen
            
            else: # If seen
                return True

        # If no numbers are seen multiple times
        return False
