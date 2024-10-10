class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for c in operations:
            if c=='D':
                ans.append(2*ans[-1])
            elif(c=='+'):
                ans.append(ans[-1]+ans[-2])
            elif(c=='C'):
                ans.pop()
            else:
                ans.append(int(c))
        return sum(ans)

        