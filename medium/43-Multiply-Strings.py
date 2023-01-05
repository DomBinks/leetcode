class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0 # Integer version of num1
        number2 = 0 # Integer version of num2

        # Convert num1 from a string to an int
        for i in range(len(num1)):
            number1 *= 10
            number1 += int(num1[i])
        
        # Convert num2 from a string to an int
        for i in range(len(num2)):
            number2 *= 10
            number2 += int(num2[i])

        # Find the product of the 2 numbers
        product = number1 * number2

        # Return the string of the product
        return str(product)