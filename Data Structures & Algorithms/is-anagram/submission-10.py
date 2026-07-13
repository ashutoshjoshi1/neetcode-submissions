class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            ds = dict()
            dt = dict()
            # c = [0]*26
            for i in range(len(s)):
                ds[s[i]] = ds.get(s[i],0)+1
                dt[t[i]] = dt.get(t[i],0)+1
            if ds == dt:
                print(ds.items(), dt.items())
                return True
        return False