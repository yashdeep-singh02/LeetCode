class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        count = 0
        n = len(s)
        m = len(t)
        while(i<n and j<m):
            if s[i]==t[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        
        if count==n:
            return True
        else:
            return False



        