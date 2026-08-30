import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        freq = Counter(nums)
        for n, f in freq.items():
            if len(h) < k:
                heapq.heappush(h, (f,n))
            elif h[0][0] < f:
                heapq.heappop(h)
                heapq.heappush(h, (f,n))
        res = []
        for f, n in h:
            res.append(n)
        return res