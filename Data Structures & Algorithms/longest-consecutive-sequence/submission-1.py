from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        store = {}

        for num in sorted(set(nums)):
            if num - 1 in store:
                store[num] = store.pop(num-1)
                store[num].append(num)
            else:
                store[num] = [num]

  
        return max([len(s) for s in store.values() ])
   

