class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(ch for ch in s.lower() if ch.isalnum())
        print(clean_s)
        return clean_s == clean_s[::-1]