class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        minPrice=prices[0]+prices[1]
        if money-minPrice>=0:
            return money-minPrice
        else:
            return money
        