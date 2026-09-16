from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        cnt = defaultdict()

        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1

        cnt_sorted = dict(sorted(cnt.items(), key=lambda item: item[1], reverse=True))
        return list(cnt_sorted.keys())[:k]
          

        