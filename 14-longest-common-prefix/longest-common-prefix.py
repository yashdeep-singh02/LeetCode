class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        i=0
        ans=""
        while i<len(strs[0]):
            if strs[0][i]==strs[-1][i]:
                ans+=strs[0][i]
                i+=1
            else:
                 break
        return ans

        