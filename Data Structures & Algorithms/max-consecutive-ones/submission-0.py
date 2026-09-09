class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        count = 0

        for num in nums:
            if num != 1:
                count = 0

            else:
                count+=1
                maxOnes = max(maxOnes, count)
        
        return maxOnes
        