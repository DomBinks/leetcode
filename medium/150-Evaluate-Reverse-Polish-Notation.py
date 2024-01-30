class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Return the last item left on the stack as it's the answer
        return int(self.recur(tokens)[0])

    # Recursive function used to evaluate the expression
    def recur(self, tokens: List[str]) -> List[str]:
        operator = "" # Operator of the operation
        operand1 = "" # First operand
        operand2 = "" # Second operand

        # If the top token is an operator 
        if tokens[-1] in ["+", "-", "*", "/"]:
            operator = tokens[-1] # Get the operator
            tokens = tokens[:-1] # Remove the operator from the stack

            # If the top token is a number
            if all([i in "0123456789" for i in tokens[-1]]):
                operand1 = tokens[-1] # Get the operand
                tokens = tokens[:-1] # Remove the operand from the stack
    
            # If the top token is an operator, meaning a subexpression needs to be evaluated
            else:
                tokens = self.recur(tokens) # Recursively evaluate the subexpression
                operand1 = tokens[-1] # Get the operand
                tokens = tokens[:-1] # Remove the operand from the stack
    
            # If the top token is a number
            if all([i in "0123456789" for i in tokens[-1]]):
                operand2 = tokens[-1] # Get the operand
                tokens = tokens[:-1] # Remove the operand from the stack
    
            # If the top token is an operator, meaning a subexpression needs ot be evaluated
            else:
                tokens = self.recur(tokens) # Recursively evaluate the subexpression
                operand2 = tokens[-1] # Get the operand
                tokens = tokens[:-1] # Remove the operand from the stack

            # Convert the operands to integers
            operand1 = int(operand1)
            operand2 = int(operand2)
    
            # Perform the correct operation for the given operator, put the result on the stack,
            # and return the stack
            if operator == "+":
                tokens.append(str(operand2 + operand1))
                return tokens
    
            elif operator == "-":
                tokens.append(str(operand2 - operand1))
                return tokens
    
            elif operator == "*":
                tokens.append(str(operand2 * operand1))
                return tokens
    
            else:
                tokens.append(str(int(operand2 / operand1)))
                return tokens

        # If the top token isn't an operator then we're done
        else:
            return tokens
