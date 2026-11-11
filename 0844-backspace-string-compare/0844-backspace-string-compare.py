class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] is not '#':
                stack.append(s[i])
            elif s[i] is '#' and stack != []:
                stack.pop(-1)
        s = "".join(stack)
        stack = []
        for i in range(len(t)):
            if t[i] is not '#':
                stack.append(t[i])
            elif t[i] is '#' and stack != []:
                stack.pop(-1)
        t = "".join(stack)
        return s == t