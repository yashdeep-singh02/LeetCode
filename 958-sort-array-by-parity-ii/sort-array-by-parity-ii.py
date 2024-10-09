class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
       
        ans=[]
        even=[]
        odd=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                even.append(nums[i])
            elif nums[i]%2!=0:
                odd.append(nums[i])
        k=0
        j=0
        m=0
        n=0
        while j<len(nums):
            if k%2==0:
                ans.append(even[m])
                k+=1
                m+=1
            else:
                ans.append(odd[n])
                k+=1
                n+=1
            j+=1
        
        return ans

        
        return nums