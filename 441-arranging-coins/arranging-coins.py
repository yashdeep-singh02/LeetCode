class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r=1,n
        res=0
        while l<=r:
            mid=(l+r)//2
            coins=(mid+1)*(mid/2)
            if coins>n:
                r=mid-1
            else:
                l=mid+1
                res=max(res,mid)
                #res=mid

        return res
        