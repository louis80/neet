class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights: 
            return 0

        i, j = 0, len(heights)-1
        maxUnits = 0 

        while i < j:
            currMaxUnits = (j - i) * min(heights[i], heights[j])

            if currMaxUnits > maxUnits:
                maxUnits = currMaxUnits
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1

        return maxUnits
