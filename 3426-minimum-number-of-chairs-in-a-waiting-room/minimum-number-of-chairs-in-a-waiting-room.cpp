class Solution {
public:
    int minimumChairs(string s) {
        stack<int> st;
        int size = s.size();
         int max = 0;
        for(int i=0;i<size;i++)
           {
             if(s[i]=='E')
                {st.push(1);
                 if (st.size()>max)
                    max=st.size();
                 }
             else 
                st.pop();
           }
        return max;
    }
};