class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 0
            else:
                d[nums[i]] += 1
        return max(d, key = d.get)