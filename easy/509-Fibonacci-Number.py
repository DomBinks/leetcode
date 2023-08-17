class Solution:
    def fib(self, n: int) -> int:
        f = [] # Stores the nth Fibonacci number
        f.append(0) # Initialise the 1st number
        f.append(1) # Initialise the 2nd number

        # For each Fibonacci number to and including n
        for i in range(2, n+1):
            # Calculate the number
            f.append(f[i-1]+f[i-2])

        # Return the nth Fibonacci number
        return f[n]
