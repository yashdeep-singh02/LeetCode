class Solution {
    public int countPartitions(int[] nums) {
        int left = nums[0];
        int right = 0,count =0;
        for(int i =1;i<nums.length;i++)
        {
            right += nums[i];
        }
        int j = 1;
       while(j<nums.length)
       {
        if((right-left)%2 ==0)
            count++;
        right=right-nums[j];
        left=left+nums[j];
        j++;
       }
       
        return count;
    }
}