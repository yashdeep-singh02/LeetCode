class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate,missing = -1,-1
        for num in nums:
            index=abs(num)-1
            if nums[index]<0:
                duplicate=abs(num)
            else:
                nums[index]*=-1     



        for i in range(len(nums)):
            if nums[i]>0:
                missing=i+1
        return [duplicate,missing]

        