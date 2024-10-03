class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        merged =""
        a = len(word1)
        b = len(word2)
        i = 0
        j = 0
        while i<a and j<b:
            if count%2 == 0:
                merged+=word1[i]
                i+=1
                count+=1
            else:
                merged+=word2[j]
                j+=1
                count+=1
        if i<a:
            merged+=word1[i:]
        elif j<b:
            merged+=word2[j:]

        return merged
            
        
        