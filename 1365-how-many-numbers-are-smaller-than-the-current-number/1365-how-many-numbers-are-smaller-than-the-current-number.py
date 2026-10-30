class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        lst = []
        c = 0
        for i in nums:
            for j in nums:
                if i>j:
                    c += 1
            lst.append(c)
            c = 0
        return lst