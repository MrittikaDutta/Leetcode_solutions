class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}             # lake -> last day it was filled
        dry_days = []         # indices where we can dry
        import bisect

        for i, lake in enumerate(rains):
            if lake == 0:
                # We can choose a lake to dry later
                bisect.insort(dry_days, i)
                ans[i] = 1    # default (will be replaced if used)
            else:
                if lake in full:
                    # We must find a dry day after the previous rain day
                    prev_day = full[lake]
                    j = bisect_right(dry_days, prev_day)
                    if j == len(dry_days):
                        # No dry day available after previous fill
                        return []
                    dry_day = dry_days[j]
                    ans[dry_day] = lake   # dry this lake on that day
                    dry_days.pop(j)       # remove that dry day
                full[lake] = i
                ans[i] = -1               # raining day → -1
        return ans
