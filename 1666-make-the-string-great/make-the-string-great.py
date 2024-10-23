class Solution:
    def makeGood(self, s: str) -> str:
        ans=''
        n = len(s)
        if(n==0 or n==1):
            return s
        i=0
        while(i< n):
            if i<n-1 and s[i]!=s[i+1] and s[i].lower()==s[i+1].lower():
                i+=2
            elif len(ans)>0 and ans[-1]!=s[i] and ans[-1].lower()==s[i].lower():
                ans = ans[:-1]
                i+=1
            else:
                ans+=s[i]
                i+=1
        
        return ans

        