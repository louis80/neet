class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
            
        max_len = 0
        left = 0
        chars = {}

        for right, char in enumerate(s):         
            if char in chars and chars[char] >= left:
                left = chars[char] + 1

            chars[char] = right 
            max_len = max(max_len, right - left + 1)
          

        return max_len

