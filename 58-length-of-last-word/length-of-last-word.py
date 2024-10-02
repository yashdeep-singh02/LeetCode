class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Strip leading and trailing spaces, then split the string by spaces
        words = s.strip().split()

        return len(words[-1]) if words else 0
        