class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict={}
        ans=-1
        for c in s:
            char_dict[c]=char_dict.get(c,0)+1
        
        for i in range(len(s)):
            if char_dict[s[i]]==1:
                return i

        
        return -1