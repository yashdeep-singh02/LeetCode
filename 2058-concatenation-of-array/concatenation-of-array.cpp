class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int>ans;
        int size = nums.size();
        for(int i=0; i < 2*size;i++)
            {
                if(i<size)
                   ans.push_back(nums[i]);
                else
                   ans.push_back(nums[i-size]);
        
            }
        return ans;
    }
};