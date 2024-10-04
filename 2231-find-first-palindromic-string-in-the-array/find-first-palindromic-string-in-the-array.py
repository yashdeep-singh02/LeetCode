class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(word):
            if word == word[::-1]:
                return True
        
        for c in words:
            if isPalindrome(c):
                return c
            else:
                continue

        return ""


