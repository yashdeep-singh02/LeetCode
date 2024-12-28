class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        n=len(nums2)
        for num in nums1:
            j=nums2.index(num)
            while j<n:
                if nums2[j]>num:
                    ans.append(nums2[j])
                    break
                elif (j==n-1):
                    ans.append(-1)
                    break                 
                j=j+1

        return ans

        