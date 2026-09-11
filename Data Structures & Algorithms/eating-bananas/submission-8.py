class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        bestRate = r

        while l <= r:
            rate = l + (r - l) // 2

            total_hours = 0

            for b in piles:
                total_hours += math.ceil(b / rate)
            
            if total_hours > h:
                l = rate + 1

            else:
                r = rate - 1
                bestRate = min(bestRate, rate)
        
        return bestRate
        






        