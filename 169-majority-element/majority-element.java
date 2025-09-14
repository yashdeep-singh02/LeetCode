import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> nm = new HashMap<>();
        int res = nums[0];    // majority element candidate
        int maxFreq = 0;      // highest frequency seen

        for (int num : nums) {
            nm.put(num, nm.getOrDefault(num, 0) + 1);

            if (nm.get(num) > maxFreq) {
                maxFreq = nm.get(num); // update max frequency
                res = num;             // update majority element
            }
        }

        return res;
    }
}
