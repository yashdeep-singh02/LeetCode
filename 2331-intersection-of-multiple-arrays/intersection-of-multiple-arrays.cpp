class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
       map<int,int>m;
        int n = nums.size(); 
        vector<int>result;
        for(int i = 0;i<n; i++)
            {
                for(int j = 0; j<nums[i].size(); j++)
                   {
                       m[nums[i][j]]++;
                   }
            }
        for(auto a:m)
            {
                if(a.second==n)
                   result.push_back(a.first);
            }
        return result;
    }
};