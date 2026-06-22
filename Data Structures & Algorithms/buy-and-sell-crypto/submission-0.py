class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for i in range(1,len(prices)):
            maxP = max(maxP, prices[i]-minBuy)
            minBuy = min(minBuy, prices[i])
        
        return maxP
        