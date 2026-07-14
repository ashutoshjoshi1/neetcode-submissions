class Solution:
    def isPalindrome(self, s: str) -> bool:
        # x = re.sub(r'[^a-zA-Z0-9]', '',s.replace(' ','').lower())
        x = ''
        for i in s:
            if i.isalnum(): x += i.lower()
        return x == x[::-1]