class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #O(N)
        mini = r

        while l <= r: #O(Log(R))
            k = l + (r - l) // 2

            #O(N) Hour Simulation Count
            hours = 0
            for bananas in piles:
                hours += self.eatBananas(bananas, k)

            if hours <= h: #Decrease banan eating rate
                mini = k
                r = k - 1
            else: #Increase bana eating rate
                l = k + 1

        return mini

    def eatBananas(self, bananas, eatRate):
        hours = math.ceil(float(bananas)/eatRate)
        return hours


        