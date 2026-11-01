class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        lst = [1] * n
        l = r = 1
        for i in range(n):
            lst[i] = l
            l *= nums[i]
        for i in range(n-1, -1, -1):
            lst[i] *= r
            r *= nums[i]
        return lst