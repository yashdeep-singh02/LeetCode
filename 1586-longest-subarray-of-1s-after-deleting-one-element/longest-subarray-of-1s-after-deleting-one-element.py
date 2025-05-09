class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count=0
        left=0
        max_size=0
        
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1

            while zero_count>1:
                if nums[left]==0:
                    zero_count-=1
                left+=1


            max_size=max(max_size, right-left)
                
            
            
        return max_size




        