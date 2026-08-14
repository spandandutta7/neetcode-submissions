class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxP = 0

        for price in prices:
            lowestPrice = min(lowestPrice, price)
            maxP = max(maxP, (price - lowestPrice))
        
        return maxP


        