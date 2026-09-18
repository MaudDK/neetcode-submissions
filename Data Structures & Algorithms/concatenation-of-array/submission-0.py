class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        m = n * 2
        ans = [0] * m

        for i in range(m):
            j = i % n
            ans[i] = nums[j]
        
        return ans

        
        