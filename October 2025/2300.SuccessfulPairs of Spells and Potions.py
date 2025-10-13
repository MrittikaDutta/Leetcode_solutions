from bisect import bisect_left
from math import ceil
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        res = []

        for spell in spells:
            required = (success + spell - 1) // spell 
            
            # Find first potion >= required
            # idx
            idx = bisect_left(potions, required)
            
            # Count of successful potions
            res.append(m - idx)
        
        return res






