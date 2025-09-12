class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer,Integer> nmap = new HashMap<>();
        int n = nums.length;

        for(int i =0;i<n;i++){

            nmap.put(nums[i],i);
        }

        for(int i=0;i<n;i++){

            int complement = target -nums[i];
            if(nmap.containsKey(complement)  && nmap.get(complement)!=i)
                   return new int[]{i,nmap.get(complement)};
        }
                return new int[]{}; // No solution found

        
    }
}