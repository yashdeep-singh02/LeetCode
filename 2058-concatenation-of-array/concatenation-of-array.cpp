class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int>ans;
        int size = nums.size();
        for(int i=0; i < 2*size;i++)
            {
              
                   ans.push_back(nums[i%size]);
                
        
            }
        return ans;
    }
};