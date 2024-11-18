class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        set_nums = sorted(set(nums))
        n = len(set_nums)
        if (n>=3):
            return set_nums[n-3]
        else:
            return set_nums[-1]
         