class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights: 
            return 0

        i, j = 0, len(heights)-1
        res = 0 

        while i < j:
            currArea = (j - i) * min(heights[i], heights[j])
            res = max(res, currArea)
           
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return res

        # space: O(n)
        # time: O(1)
