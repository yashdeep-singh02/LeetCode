class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_1 = {}
        ans=[]
        i=0
        while(i<len(nums)):
            v = target-nums[i]
            value = dict_1.get(v,"-1")
            if value!= "-1":
                ans.append(value)
                ans.append(i)
                break
            else:
                dict_1[nums[i]]=i
            i+=1
        return ans

        