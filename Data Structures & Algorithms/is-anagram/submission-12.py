class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     ds = dict()
        #     dt = dict()
        #     for i in range(len(s)):
        #         ds[s[i]] = ds.get(s[i],0)+1
        #         dt[t[i]] = dt.get(t[i],0)+1
        #     if ds == dt:
        #         print(ds.items(), dt.items())
        #         return True
        # return False
        if len(s) != len(t):
            return False
        c = [0] * 26
        for i in range(len(s)):
            c[ord(s[i])-ord('a')] += 1
            c[ord(t[i])-ord('a')] -= 1
        for i in c:
            if i != 0:
                return False
        return True