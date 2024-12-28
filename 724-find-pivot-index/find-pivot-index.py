class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum=0
        rsum=sum(nums)
        i=0
        while i<len(nums):
            rsum=rsum-nums[i]
            if i>0:
                lsum=lsum+nums[i-1]
            if lsum==rsum:
                return i
            
            i=i+1
        
        return -1
        