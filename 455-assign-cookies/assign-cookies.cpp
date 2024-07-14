class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        int cNums = s.size();
        if(cNums==0) return  0;
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());

        int maxNum = 0;
        int cookieIndex = cNums - 1;
        int childIndex = g.size() - 1;
        while(cookieIndex>= 0 && childIndex>=0)
           {
            if(s[cookieIndex]>=g[childIndex])
               {
                maxNum++;
                cookieIndex--;
                childIndex--;
               }
               else
                  {
                    childIndex--;
                  }
           }
        return maxNum;
    }
};