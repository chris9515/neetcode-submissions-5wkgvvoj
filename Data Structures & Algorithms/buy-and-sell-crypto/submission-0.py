class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        res = 0
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            res = max(res, prices[i]-low)
        return res
            
            