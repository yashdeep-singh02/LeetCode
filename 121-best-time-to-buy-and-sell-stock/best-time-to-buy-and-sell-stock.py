class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        cheapest=float('inf')
        for price in prices:
            
            if cheapest>price:
                cheapest=price
            else:
                maxProfit=max(maxProfit,price-cheapest)

        return maxProfit
        