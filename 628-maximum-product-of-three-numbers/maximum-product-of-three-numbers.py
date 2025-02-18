class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]>=0:
            return nums[-1]*nums[-2]*nums[-3]
        elif nums[0]<0 and nums[-1]<0:
            return nums[-1]*nums[-2]*nums[-3]
        else:
            x=nums[0]*nums[1]
            y=nums[-2]*nums[-3]
            return x*nums[-1] if x>y else y*nums[-1]