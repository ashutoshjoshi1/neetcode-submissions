class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        ans = []
        for i in nums:
            seen[i] += 1
        sortd = dict(sorted(seen.items(), key=lambda item: item[1], reverse = True))
        return list(sortd.keys())[:k]