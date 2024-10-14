class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans=0
        i=1

        while(n>=i):
            n=n-i
            if n>=0:
               ans+=1
            i+=1
        return ans
        