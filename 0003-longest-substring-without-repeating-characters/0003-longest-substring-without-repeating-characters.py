class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = temp = ''
        for i in range(len(s)):
            if s[i] not in temp:
                temp += s[i]
            else:
                if len(temp) > len(res):
                    res = temp
                idx = temp.index(s[i])
                temp = temp[idx + 1:] + s[i]
        if len(temp) > len(res):
            res = temp
            
        return len(res)