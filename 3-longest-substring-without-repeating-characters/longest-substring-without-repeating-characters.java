class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        char[] c= s.toCharArray();
        int l=0,maxcount=0;
        for(int r=0;r<s.length();r++)
        {
            if(map.containsKey(c[r]))
            {
                l=Math.max(l,map.get(c[r])+1);
            }
            
        
                map.put(c[r],r);
                maxcount = Math.max(r-l+1,maxcount);

            
                   
        }

        return maxcount;
        
    }
}