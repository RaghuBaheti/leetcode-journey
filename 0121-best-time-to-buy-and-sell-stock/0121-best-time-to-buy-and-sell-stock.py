class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float('inf')
        maxi = 0
        for price in prices:
            maxi = max(maxi, price - mini)
            if price < mini:
                mini = price
        return maxi