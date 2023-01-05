from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        coins.reverse()

        numCoins = 0
        currentValue = 0
        for coin in coins:
            while amount - currentValue >= coin:
                numCoins += 1
                currentValue += coin
        
        if(currentValue == amount):
            return numCoins
        
        else:
            return -1