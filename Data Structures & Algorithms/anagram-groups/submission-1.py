class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        # for i in strs:
        #     si = ''.join(sorted(i))
        #     d[si].append(i)
        # return list(d.values())

        for i in strs:
            c = [0]*26
            for x in i:
                c[ord(x)-ord('a')] += 1
            d[tuple(c)].append(i)
        return list(d.values())

        