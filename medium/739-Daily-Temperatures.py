class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = deque() # Stack to store the indicies of temps. waiting for an increase
        waiting.append(0) # Add 0 to the stack to start

        when = [0] * len(temperatures) # Stores when the temp. increases for each index

        # For each temperature after the first temperature
        for i in range(1, len(temperatures)):
            # While there are indices waiting for a temperature increase
            # and this temperature is warmer than the temperature at the top of the stack
            while len(waiting) != 0 and temperatures[i] > temperatures[waiting[-1]]:
                # Set the amount of days waited to the difference between the index
                # waiting for the increase and this index
                when[waiting[-1]] = i - waiting[-1]
                # Remove this index from the top of the stack
                waiting.pop()

            # Add this index to the stack
            waiting.append(i)

        return when
