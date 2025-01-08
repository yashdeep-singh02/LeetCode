class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      
        numsum=sum(nums)
        leftsum=0
        rightsum=numsum
        n=len(nums)
        i=0
        while i<n:
            if i>0:
                leftsum=leftsum+nums[i-1]
            rightsum=rightsum-nums[i]
            if leftsum==rightsum:
                return i
            i=i+1
        

        return -1
        
           
          
        