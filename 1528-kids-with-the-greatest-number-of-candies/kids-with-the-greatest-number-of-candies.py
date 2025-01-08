class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandies=max(candies)
        ans=[]
        for c in candies:
            if c+extraCandies>=maxcandies:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans
        