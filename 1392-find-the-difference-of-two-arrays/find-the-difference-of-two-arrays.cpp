class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
            vector<vector<int>>result;
            vector<int>r1;
            vector<int>r2;
            unordered_set<int>n1(nums1.begin(),nums1.end());
            unordered_set<int>n2(nums2.begin(),nums2.end());
            for(auto a:n2)
             {                
                if(n1.find(a) != n1.end())
                       continue;
                else
                    r1.push_back(a);

                      
             }
              for(auto a:n1)
             {                
                if(n2.find(a) != n2.end())
                    continue;
                else
                    r2.push_back(a);

                      
             }
            result.push_back(r2);
            result.push_back(r1);
            return result;
    }
};