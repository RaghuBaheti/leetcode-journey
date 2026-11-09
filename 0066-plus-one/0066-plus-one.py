class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''
        for i in digits:
            s += str(i)
        s = str(int(s) + 1)
        res = [0] * len(s)
        for i in range(len(s)):
            res[i] = int(s[i])
        return res