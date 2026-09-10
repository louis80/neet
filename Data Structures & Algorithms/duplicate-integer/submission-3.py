class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i in nums: 
            v = cnt.get(i, 0)
            if v == 1:
                return True
            cnt[i] = cnt.get(i, 0) + 1

        return False