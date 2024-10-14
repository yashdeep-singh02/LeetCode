class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        mid=0
        while(l<=r):
            mid=(l+r)//2
            midsq=mid*mid
            if  midsq>x:
                r=mid-1
            elif midsq<x:
                l=mid+1
            else:
                return mid
        return r

        