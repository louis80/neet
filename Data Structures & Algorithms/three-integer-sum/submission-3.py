class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums: 
            return []

        triplets = set()
        nums.sort()
        # -4,-1,-1,0,1,2

        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i+1, len(nums)):
                target = -(nums[i] + nums[j])
                
                if target in seen: 
                    triplets.add((nums[i], target, nums[j]))

                seen.add(nums[j])

        return list([t for t in triplets])




