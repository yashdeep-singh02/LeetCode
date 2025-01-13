class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i=0
        j=len(nums)-1
        nums.sort()
        ans=0
        while i<j:
            x = nums[i]+nums[j]
            if x==k:
                ans+=1
                i+=1
                j-=1
            elif x<k:
                i+=1
            else:
                j-=1
        
        return ans
            
        