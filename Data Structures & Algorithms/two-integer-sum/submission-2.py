class Solution:
    # Input: nums=[3,4,5,6]
    #=[3,4,5,2]
    #target=7
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return 

        #{3: 0, 3: 1}
        obs = {} # value : index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in obs:
                return [obs[diff], i]
            else:
                obs[nums[i]] = i

        return []

        