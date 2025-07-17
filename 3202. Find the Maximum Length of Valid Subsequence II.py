from typing import List
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod_val = (nums[i] + nums[j]) % k
                # extend j's subsequence with this mod_val
                dp[i][mod_val] = max(dp[i][mod_val], dp[j][mod_val] + 1)
            # Each single element counts as a sequence of length 1
            for mod_val in dp[i]:
                max_len = max(max_len, dp[i][mod_val] + 1)

        return max_len
