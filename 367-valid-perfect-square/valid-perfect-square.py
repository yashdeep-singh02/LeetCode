class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=1
        r=num
        while l<=r:
            mid=(l+r)//2
            sqmid=mid*mid
            if sqmid==num:
                return True
            elif(sqmid>num):
                r=mid-1
            else:
                l=mid+1
        return False
        