from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            x = 0
            for i in account:
                x += i

            if x > max:
                max = x

        return max 