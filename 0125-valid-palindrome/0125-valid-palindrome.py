class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''
        for i in s:
            if i.isalnum():
                t += i
        t = t.lower()
        return t == t[::-1]