from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # Tracks how many times each number is seen

        # For each number
        for num in nums:
            # If the number has been seen before
            if num in seen:
                # Increment the times seen
                seen[num] += 1
            # If the number hasn't been seen before
            else:
                # Set the times seen to 1
                seen[num] = 1

        # Store the key value pairs in an array, with the first value being
        # the negative value, so it can be used to create a max priority queue
        pq = [(-value, key) for key, value in seen.items()]

        # Convert the array into a priority queue
        heapify(pq)

        out = [] # Stores the output

        # Do k times
        for i in range(0, k):
            # Get the pair from the top of the PQ - has highest frequency
            a = heappop(pq)
            # Add the number with that frequency to the output array
            out.append(a[1])

        return out
