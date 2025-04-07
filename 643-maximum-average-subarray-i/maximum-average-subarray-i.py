class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # max_average = float('-inf')
        add= sum(nums[0:k])
        max_sum=add
        i=k
        while i < len(nums):
            add=add+nums[i]-nums[i-k]
            max_sum=max(max_sum,add)
            i=i+1
        return max_sum/k
        