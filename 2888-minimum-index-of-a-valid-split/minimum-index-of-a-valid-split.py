class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n= len(nums)
        for i in nums:
            if nums.count(i)>n/2:
                dom = i
                c=nums.count(i)
                break
        i=0
        count=0
        while i < n-1:
            if nums[i]==dom:
                count+=1
                if count>(i+1)/2 and (c-count)>(n-i-1)/2:
                    return i
            i+=1

        return -1







        