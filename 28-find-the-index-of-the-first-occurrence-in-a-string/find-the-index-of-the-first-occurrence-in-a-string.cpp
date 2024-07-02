class Solution {
public:
    int strStr(string haystack, string needle) {
        int size1= haystack.size();
        int size2 = needle.size();
        if(size1==size2 )
           {
            if(haystack==needle)
               return 0;
           }
        int ans=-1;
        for(int i=0;i<size1;i++)
           {
             if(haystack[i]==needle[0])
                   {
                    int count = 0;
                    for(int j=0;j<size2;j++)
                       {
                          if(needle[j]==haystack[i+j])
                             {count++;
                              if(count==size2)
                                 return i;
                             }

                        else 
                            break;
                       } 
                   }
             else 
                continue;
           }



        return ans;
    }
};