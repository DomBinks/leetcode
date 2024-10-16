class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        alive = [0] * 2051 # Stores how many are alive in each year
        
        # Loop over all log entries
        for entry in logs:
            # For all years they're alive
            for i in range(entry[0], entry[1]):
                # Increment the amount alive for that year
                alive[i] += 1

        i = 1950 # Starting at the earliest year
        m = max(alive) # Year where maximum are alive

        # Find the year where the maximum are alive
        while alive[i] != m:
            i += 1

        return i
