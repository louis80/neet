class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        cnt_s, cnt_t = {}, {}

        for l in s:
            cnt_s[l] = cnt_s.get(l, 0) + 1 

        for l in t:
            cnt_t[l] = cnt_t.get(l, 0) + 1 

        return cnt_s == cnt_t