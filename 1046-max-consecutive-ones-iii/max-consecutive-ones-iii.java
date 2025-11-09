class Solution {
    public int longestOnes(int[] nums, int k) {
        int l =0,zeroes = 0, len=0,maxlen=0;
        for(int r=0;r<nums.length;r++)
        {
            if(nums[r]==1)
                len++;
            else if(nums[r]==0 && zeroes<k)
                {
                    len++;
                    zeroes++;
                }
            else
             { 
                    maxlen= Math.max(len,maxlen);
                    zeroes++;
                    len++;
                    while(zeroes>k)
                    {
                        if(nums[l]==0)
                        {
                            zeroes--;
                        }
                        len--;
                        l++;
                    }

            }
        }
        maxlen= Math.max(len,maxlen);

        return maxlen;
    }
}