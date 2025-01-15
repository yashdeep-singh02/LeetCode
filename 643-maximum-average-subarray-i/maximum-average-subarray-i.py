class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=k
        j=len(nums)
        current_sum=sum(nums[0:k])
        max_sum=current_sum


        while(i<j):
            current_sum=current_sum-nums[i-k]+nums[i]
            max_sum=max(max_sum,current_sum)
            i+=1

        return max_sum/k
        