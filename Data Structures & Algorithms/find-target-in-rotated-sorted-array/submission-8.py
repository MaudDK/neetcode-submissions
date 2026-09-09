class Solution:
    def search(self, nums: List[int], target: int) -> int:    
        pivot = self.findMin(nums)
        
        if nums[pivot] <= target <= nums[-1]:
            index = self.binary_search(nums, target, l = pivot, r = len(nums) - 1)
        else:
            index = self.binary_search(nums, target, l = 0, r = pivot - 1)
        
        return index
    
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return l

    def binary_search(self, nums, target, l, r):
        while l <= r:
            m = l + (r - l) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
    
        return -1








        