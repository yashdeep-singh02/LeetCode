class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_string = ''.join(char.lower() for char in s if char.isalnum())
        i , j = 0, len(processed_string)-1
        while(i<=j):
            if processed_string[i]!=processed_string[j]:
                return False
            i+=1
            j-=1
        
        return True

        