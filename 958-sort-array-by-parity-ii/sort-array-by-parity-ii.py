class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
       
        ans=[]
        even=[]
        odd=[]
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
      
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even.pop())
               
            else:
                ans.append(odd.pop())
                
        
        return ans

        
        return nums