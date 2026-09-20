class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0

        maxP = 0
        minBuy = prices[0]

        # [10,1,5,6,7,1]

        for p in prices:
            maxP = max(maxP, p - minBuy)
            minBuy = min(minBuy, p)

        return maxP        