class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return helper(nums,k) - helper(nums,k-1);
    }

    public int helper(int[]nums, int maxOdd)
    {
        if(maxOdd<0)
            return 0;

        int l=0, count =0, ans =0;

        for(int r=0;r<nums.length;r++)
        {
            if(nums[r]%2!=0)
                    count++;

            while(count>maxOdd)
            {
                if(nums[l]%2!=0)
                    {
                        count--;
                    }
                l++;
            }
          ans+=(r-l+1);
        }
        return ans;
    }
}