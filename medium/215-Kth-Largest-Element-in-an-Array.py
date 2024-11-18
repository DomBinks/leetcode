class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for n in nums:
            h.append(-n)
        
        heapq.heapify(h)

        r = None
        for i in range(k):
            r = heapq.heappop(h)

        return -r
