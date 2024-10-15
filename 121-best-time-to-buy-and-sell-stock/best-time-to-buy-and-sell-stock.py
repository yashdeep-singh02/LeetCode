class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        cheapest=100000
        for i in range(len(prices)):
            
            if i>0 :
                profit=prices[i]-cheapest
                if profit>maxProfit:
                    maxProfit = profit
            if cheapest>prices[i]:
                cheapest=prices[i]

        return maxProfit
        