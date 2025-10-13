from collections import Counter
from bisect import bisect_left
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        if not power:
            return 0
        total = defaultdict(int)
        for v in power:
            total[v] += v

        vals = sorted(total.keys())                # distinct damage values sorted
        n = len(vals)
        dp = [0] * n

        for i, v in enumerate(vals):
            weight = total[v]
            # find rightmost index j with vals[j] <= v - 3
            j = bisect.bisect_right(vals, v - 3) - 1
            take = weight + (dp[j] if j >= 0 else 0)
            not_take = dp[i-1] if i > 0 else 0
            dp[i] = max(take, not_take)

        return dp[-1]
