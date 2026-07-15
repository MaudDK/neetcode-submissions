class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = dict()

        for i, num in enumerate(nums):
            c = target - num
            if c in prev_map:
                return [prev_map[c], i]
            prev_map[num] = i
        
        return []