class Solution:
    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        occurrences = []
        ans = []
        i = 0
        while i < len(nums):
            if nums[i] == x:
                occurrences.append(i)
            i+=1

        for i in queries:
            if len(occurrences)<i:
                ans.append(-1)
            else:
                ans.append(occurrences[i-1])

        return ans
