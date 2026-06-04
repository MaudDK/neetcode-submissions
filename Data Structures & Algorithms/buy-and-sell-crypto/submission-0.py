class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        l = 0

        for r in range(len(prices)):
            p = prices[r] - prices[l]

            if prices[r] < prices[l]:
                l = r

            max_p = max(max_p, p)
        
        return max_p
           