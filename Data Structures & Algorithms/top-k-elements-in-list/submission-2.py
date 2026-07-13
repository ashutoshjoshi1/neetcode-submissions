class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = 1 + d.get(i,0)
        sort_d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        # res = []
        # for i in range(k):
        #     res.append(list(sort_d.keys())[i])
        return list(sort_d.keys())[0:k]

        