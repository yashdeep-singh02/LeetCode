class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int size = nums.size();
        int l=0;
        int r = size-1;
        int pos = size-1;
        vector<int>ans(size);
        while(r>=l)
        {
           if(abs(nums[l])<abs(nums[r]))
                {
                    ans[pos--]=nums[r]*nums[r];
                    r--;
                }
            else{
                ans[pos--]=nums[l]*nums[l];
                l++;
            }
        }
        return ans;
    }
};