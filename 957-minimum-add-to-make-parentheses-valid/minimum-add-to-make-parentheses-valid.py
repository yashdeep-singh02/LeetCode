class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op=0
        cl=0
        for ch in s:
            if ch==')' and op==0:
                cl+=1
            elif ch==")" and op>0:
                op-=1
            elif ch=="(":
                op+=1
        
        return op+cl

        