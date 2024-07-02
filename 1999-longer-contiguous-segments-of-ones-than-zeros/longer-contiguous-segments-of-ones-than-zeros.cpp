class Solution {
public:
    bool checkZeroOnes(string s) {
        int num0 =0;
        int num1 =0;
        int count0 = 0;
        int count1 = 0;
        for(int i=0;i<s.size();i++)
           {
            if(s[i]=='0')
               {
                count1= 0;
                count0++;
                if(num0<count0)
                   num0 = count0;
               }
            else 
              {
                count0 = 0;
                count1++;
                if(num1<count1)
                   num1 = count1;
               }
           }
        if(num1>num0)
            return true;
        else
          return false;
    }
};