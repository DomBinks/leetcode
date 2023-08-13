class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0 # Number of divisors of n found

        i = 1

        # While the square of i is less than or equal to n
        while i*i <= n:
            # If i is a divisor of n
            if n % i == 0:
                divisors += 1 # Increment the count

                # If the number i is multiplied by to get to n
                # isn't itself i.e. another divisor
                if i*i < n:
                    divisors += 1 # Increment the count

            i += 1 # Go to the next i

        return divisors == 3
