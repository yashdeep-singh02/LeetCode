class Solution {
public:
    bool checkOnesSegment(string s) {
        int count = 0;
        
        int size = s.size();
        // if(size<=2 && s[0]=='1')
        //     return true;
           
        for(int i=1;i<size;i++)
           {
            if(s[i]=='1' && s[i-1]=='0')
                {
                    return false;
                  }
           }
           return true;
    }
};