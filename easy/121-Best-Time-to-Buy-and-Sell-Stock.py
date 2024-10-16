class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0 # Best profit so far

        # Start both at rightmost index
        low = prices[len(prices) - 1]
        high = prices[len(prices) - 1]

        # Go from rightmost - 1 to 0 inc.
        for i in range(len(prices) - 2, -1, -1):
            # If this value is lower then it's a better
            # time to buy
            if prices[i] < low:
                low = prices[i]

            # Better to sell at this point going forward
            # as it's a new high
            if prices[i] > high:
                # Update the best to this point if best seen
                # so far
                if high - low > best:
                    best = high - low

                # Start from this point to see if this new high
                # can generate a bigger profit
                high = prices[i]
                low = prices[i]

        # Update if selling at the highest price generates
        # the biggest profit
        if high - low > best:
            best = high - low

        return best
