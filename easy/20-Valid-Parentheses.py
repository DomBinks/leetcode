class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack storing opening parentheses

        # Maps closing parentheses to their openning
        closing = {')': '(', '}': '{', ']':'['} 

        # For each character in the string
        for c in s:
            # If the character is an openning parenthesis
            if c == '(' or c == '{' or c == '[':
                stack.append(c) # Add it to the stack
                    
            # If the character is a closing parenthesis
            else:
                # If the stack is empty
                if len(stack) == 0:
                    # No correspondig openning parenthesis
                    return False

                # If the top character on the stack is the corresponding
                # parenthesis
                elif stack[len(stack)-1] == closing[c]:
                    # Remove the openning parenthesis from the stack
                    stack.pop()
                    
                # If the top character on the stack isn't the corresponding
                # parenthesis
                else:
                    return False

        # If the stack isn't empty i.e. there are unmatched openning
        # parentheses
        if stack != []:
            return False

        else:
            return True
