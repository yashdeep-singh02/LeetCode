class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
          unordered_map<int,int>count;
          vector<int>result;
          for(auto i:nums1)
             {
                count[i]++;
             }
          
          for(auto num:nums2)
              {
                if(count[num]>0)
                    {
                        result.push_back(num);
                        count[num]--;
                    }
              }
        return result;
    }
};