class Solution {
public:
    bool isSubsequence(string s, string t) {
        int s1 = s.size();
        int s2 = t.size();
        int i = 0;
        int j = 0;
        while(i<s1 && j<s2)
             {
                if(s[i]==t[j])
                    {
                        i++;
                       
                    }
                 j++;
                
             }
             if(i>=s1)
                   return true;
                return false;
    }
};