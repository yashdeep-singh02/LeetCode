class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=0
        for i in nums:
            if n<0:
                return False
            elif n<i:
                    n=i
            n-=1
        
        return True

                    

        