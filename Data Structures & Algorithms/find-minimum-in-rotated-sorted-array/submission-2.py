class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
            
            minimum = min(minimum, nums[m])
        
        return minimum
