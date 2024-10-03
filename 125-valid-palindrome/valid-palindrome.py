class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_string = ''.join(char.lower() for char in s if char.isalnum())
        return processed_string == processed_string[::-1]

        