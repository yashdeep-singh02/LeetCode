class Solution {
public:
    int maxPower(string s) {
        int count=1;
        int maxcount =1;

        for (int i=1;i<s.size();i++)
             {
                if(s[i]==s[i-1])
                   {
                    count++;
                    if(maxcount<count)
                           maxcount=count;
                   }
                else
                  count=1;
             }
        return maxcount;
    }
};