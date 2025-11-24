class Solution:
    def merge(self, intervals):
        intervals.sort()  # sort by start time
        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                # no overlap → new interval
                res.append([start, end])
            else:
                # overlap → merge with the last interval
                res[-1][1] = max(res[-1][1], end)

        return res
