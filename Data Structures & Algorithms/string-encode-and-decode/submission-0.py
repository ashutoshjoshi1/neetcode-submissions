class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            # s.append('<s>')
            s += i
            s+='<e>'
        return s
    def decode(self, s: str) -> List[str]:
        res = list(s.split('<e>'))
        res.pop()
        return res
