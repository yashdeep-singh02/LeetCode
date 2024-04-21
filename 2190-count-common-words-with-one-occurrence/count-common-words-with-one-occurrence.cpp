class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        map<string ,int> mp;
        for(auto str:words1)
            {
                if(mp[str]==0) 
                      mp[str]=1;
                else if(mp[str]==1)
                     mp[str]=-1;

            }
        for(auto str:words2)
             {
                if(mp[str]==1)
                    mp[str]=2;
                else if(mp[str]==2)
                   mp[str]=-1;
             }
         int count =0;
         for(auto i:mp)
            {
                if(i.second==2)
                     count++;              
             }
        return count;
    }
};