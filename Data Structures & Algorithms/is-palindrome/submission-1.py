class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = re.sub(r'[^a-zA-Z0-9]', '',s.replace(' ','').lower())
        return x == x[::-1]