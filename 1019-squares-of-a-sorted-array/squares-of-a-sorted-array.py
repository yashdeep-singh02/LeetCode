class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[None]*len(nums)
        l=0
        r=len(nums)-1
        k=r
        while(l<=r):
            lsq=nums[l]*nums[l]
            rsq=nums[r]*nums[r]
            if(lsq>rsq):
                ans[k]=lsq
                l+=1
            else:
                ans[k]=rsq
                r-=1

            k-=1
        return ans
        