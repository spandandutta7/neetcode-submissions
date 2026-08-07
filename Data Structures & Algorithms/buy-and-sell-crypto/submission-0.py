class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuy = prices[0]
        maxProfit = 0

        for sellPrice in prices:
            lowestBuy = min(lowestBuy, sellPrice)
            maxProfit = max(maxProfit, (sellPrice - lowestBuy))
        return maxProfit