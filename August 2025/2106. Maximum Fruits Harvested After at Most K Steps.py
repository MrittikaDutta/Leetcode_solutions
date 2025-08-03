from typing import List
from bisect import bisect_left
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        left = 0
        total = 0
        max_fruits = 0

        for right in range(n):
            total += fruits[right][1]

            # Try shrinking the window from left if movement cost exceeds k
            while left <= right:
                l_pos = fruits[left][0]
                r_pos = fruits[right][0]

                # Calculate min steps to cover the window
                min_steps = min(
                    abs(startPos - l_pos) + (r_pos - l_pos),
                    abs(startPos - r_pos) + (r_pos - l_pos)
                )

                if min_steps <= k:
                    break
                total -= fruits[left][1]
                left += 1

            max_fruits = max(max_fruits, total)

        return max_fruits
