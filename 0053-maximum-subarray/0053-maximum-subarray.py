class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        m_sum = c_sum = nums[0]
        seen = reset = 0
        for i in range(1, len(nums)):
            seen = nums[i]
            c_sum += seen
            if c_sum < nums[i]:
                c_sum = nums[i]
            m_sum = max(c_sum, m_sum)
        return m_sum