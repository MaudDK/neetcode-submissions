class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = [c.lower() for c in s if c.isalnum()]
        return alnum == alnum[::-1]

        