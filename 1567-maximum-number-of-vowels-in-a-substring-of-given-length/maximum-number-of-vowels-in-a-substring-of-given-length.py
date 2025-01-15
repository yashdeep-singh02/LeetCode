class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current_count=0
        vowel= set('aeiou')
        for i in range(0,k):
            if s[i] in vowel:
                current_count=current_count+1

        max_count=current_count

        for i in range(k,len(s)):
            if s[i] in vowel:
                current_count+=1
            if s[i-k] in vowel:
                current_count-=1
            
            max_count = max(max_count,current_count)

        return max_count
        