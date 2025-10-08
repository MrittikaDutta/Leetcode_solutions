from bisect import bisect_left
from math import ceil
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            # Minimum potion strength needed for success
            required = (success + spell - 1) // spell  # same as ceil(success / spell)
            
            # Find first potion >= required
            idx = bisect_left(potions, required)
            
            # Count of successful potions
            res.append(m - idx)
        
        return res






