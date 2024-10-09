class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i=0
        ans=[]
       
      
        while i<numRows:
            j=0
            temp=[]
            while j<=i:
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
                j+=1
            ans.append(temp)  
            i+=1
        return ans  
