class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        n = [nums[0],]
        for num in nums:
            if num != nums[i]:
                n.append(num)
                i = nums.index(num)
        nums[:] = n
        return len(nums)