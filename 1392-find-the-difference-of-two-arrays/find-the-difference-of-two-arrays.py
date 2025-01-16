class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1=set(nums1)
        n2=set(nums2)
        ans1,ans2=[],[]
        for i in n1:
            if i not in n2:
                ans1.append(i)

        for i in n2:
            if i not in n1:
                ans2.append(i)
        
        return [ans1,ans2]
