class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        min_length=float('inf')
        current_sum=0
        while j<len(nums):
            current_sum+=nums[j]
            while current_sum>=target:
                min_length= min(min_length,j-i+1)
                current_sum-=nums[i]
                i+=1
            j+=1
        if min_length<float('inf'):
            return min_length
        else:
            return 0
            
        