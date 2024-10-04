class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        i=1
        n = len(nums)
        while(i<n):
            if(nums[i]==nums[k-1]):
                i+=1
            else:
                nums[k]=nums[i]
                i+=1
                k+=1
        del nums[k:n]
            
        