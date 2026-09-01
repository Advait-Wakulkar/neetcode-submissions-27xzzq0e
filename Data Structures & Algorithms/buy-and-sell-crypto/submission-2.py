class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = float("-inf")
        for r in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxProfit = max(maxProfit, prices[r] - prices[l])
        return maxProfit        