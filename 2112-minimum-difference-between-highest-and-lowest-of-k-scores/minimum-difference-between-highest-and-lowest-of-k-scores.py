class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        j = k-1
        difference = sys.maxsize
        while j<n:
            temp = nums[j]-nums[i]
            if(difference > temp ):
                difference = temp
            
            i+=1
            j+=1
        return difference
        