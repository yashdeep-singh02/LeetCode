class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[]
        sorted_score = sorted(score,reverse=True)
        for i in range(len(score)):
            ind=sorted_score.index(score[i])
            if (ind==0):
                ans.append("Gold Medal")
            elif(ind==1):
                ans.append("Silver Medal")
            elif(ind==2):
                ans.append("Bronze Medal")
            else:
                ans.append(str(ind+1))
        return ans


        