class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        maxWidth = 0
        
        # Build a monotonic decreasing stack with candidate indices for k
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        # Iterate from the end of the array to find the maximum width ramp
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                maxWidth = max(maxWidth, j - stack.pop())

        return maxWidth
