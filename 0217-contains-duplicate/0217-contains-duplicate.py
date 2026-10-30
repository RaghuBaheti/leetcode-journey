class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d = {}
        flag = 0
        for i in range(len(nums)):
            if nums[i] in d:
                flag = 1
                break
            else:
                flag = 0
                d[nums[i]] = i
        if flag == 1:
            return True
        else:
            return False