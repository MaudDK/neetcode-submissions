class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cmap = dict()
        for i in range(len(nums)):
            c = target - nums[i]
            
            if c in cmap:
                return [cmap[c], i]
            
            cmap[nums[i]] = i


        