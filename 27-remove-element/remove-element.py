class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]==val :
                i+=1
            else:
                nums[k]=nums[i]
                k+=1
                i+=1
        del nums[k:]
        return k
        