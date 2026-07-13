class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # d = {}
        # for i in nums:
        #     d[i] = 1 + d.get(i,0)
        # sort_d = dict(sorted(d.items(), key = lambda item: item[1], reverse = True))
        # # res = []
        # # for i in range(k):
        # #     res.append(list(sort_d.keys())[i])
        # return list(sort_d.keys())[0:k]

        # count = {}
        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        # count = {}
        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


