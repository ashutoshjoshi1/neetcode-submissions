class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        ans = []
        for i in nums:
            seen[i] += 1
        sortd = dict(sorted(seen.items(), key=lambda item: item[1], reverse = True))
        for j in sortd.keys():
            ans.append(j)
        return ans[:k]