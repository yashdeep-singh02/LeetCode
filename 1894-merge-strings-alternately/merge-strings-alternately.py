class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        count=0
        j=0
        k=0
        while j<len(word1) and k<len(word2):
            if count%2 ==0:
                ans+=(word1[j])
                j+=1
            else:
                ans+=(word2[k])
                k+=1
            count+=1

        while j<len(word1):
            ans+=(word1[j])
            j+=1
        while k<len(word2):
            ans+=(word2[k])
            k+=1
        return ans

        