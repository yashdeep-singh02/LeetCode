class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        j=len(height)-1
        i=0
        while(i<j):
            area=(j-i)*min(height[j],height[i])
            max_area=max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            
        return max_area

        