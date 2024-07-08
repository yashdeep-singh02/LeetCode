class Solution {
public:
    int lengthOfLastWord(string s) {
        int alpha = 0; 
        
        int ans = 0; // Length of the last word found
        
        int i = s.size()-1;
        // Loop through the string character by character
        while(i>=0){
           if(alpha == 0 && s[i]==' ')
              {
                i--;
                continue;
              }
            else if( iswalnum(s[i]))
               {
                ans++;
                alpha =1;
                i--;
                continue;
               }
            else if(alpha==1 && s[i]==' ')
                 break;
        }
              
        return ans;
    }
};
