class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        biggest = {} # Stores the biggest 2 numbers whose digits sum to the key
        maximum = -1 # Stores the maximum sum any pair of biggest 2 numbers

        # For each number
        for i in nums:
            total = 0 # Stores the sum of the digits
            
            j = i # Copy i
            # While j has digits left
            while j > 0:
                # Add the rightmost digit to the total
                total += j % 10
                # Remove the rightmost digit from j
                j //= 10

            # If this digit sum has been seen
            if total in biggest:
                # If this number is the biggest with this digit sum
                if i > biggest[total][1]:
                    # Set the 2nd biggest number to the previous biggest number
                    biggest[total][0] = biggest[total][1]
                    biggest[total][1] = i # Set the biggest number to this number
                # If this number is the 2nd biggest with this digit sum
                elif i > biggest[total][0]:
                    biggest[total][0] = i # Set the 2nd biggest number to this number

                # If these 2 biggest numbers give the maximum sum seen so far
                if biggest[total][0] + biggest[total][1] > maximum:
                    # Update the maximum sum seen so far
                    maximum = biggest[total][0] + biggest[total][1]

            # If this digit sum hasn't been seen
            else:
                # Set this number as the biggest of the pair
                # with -1 as a placeholder
                biggest[total] = [-1,i]
        
        return maximum
