class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return nums
        if len(nums)==1:
            return [f"{nums[0]}"]
        i,j=0,1
        count=1
        ans=[]
        while j<len(nums):
            if nums[j]!=nums[j-1]+1:
                if count>1:
                    ans.append(f"{nums[i]}->{nums[j-1]}")
                else:
                    ans.append(f"{nums[i]}")
                i=j
                count=1
            else:
                count+=1
            j+=1
        if count>1:
            ans.append(f"{nums[i]}->{nums[j-1]}")
        else:
            ans.append(f"{nums[i]}")
        return ans
        



        