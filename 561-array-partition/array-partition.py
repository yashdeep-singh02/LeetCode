class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        n=len(nums)
        i=0
        for i in range(0, n, 2):            
            ans+=nums[i]
            

        return ans
            
        