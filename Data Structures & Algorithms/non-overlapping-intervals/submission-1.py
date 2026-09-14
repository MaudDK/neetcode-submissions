class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        remove = 0

        intervals.sort(key = lambda x: x[0])
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                remove+=1
                prevEnd = min(end, prevEnd)

        return remove


        