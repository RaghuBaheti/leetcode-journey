class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        s = s.rstrip()
        for char in s[::-1]:
            if char is not ' ':
                c += 1
            else:
                break
        return c