class Solution:
    def isValid(self, s: str) -> bool:
        """Returns whether the string contains correct brackets"""
        stack = [] # Stores currently opened brackets
        map = {'(': ')', '[': ']', '{': '}'}

        for i in s: # For each bracket in the input
            if i in map: # If it is an opening bracket
                stack.append(i) # Put it on the stack
            else: # If it's a closing bracket
                # If it doesn't correspond to an opening bracket
                if stack == [] or map[stack.pop()] != i:
                    return False

        if stack == []: # If there are no brackets left over
            return True 
        else: # If there are brackets left over
            return False