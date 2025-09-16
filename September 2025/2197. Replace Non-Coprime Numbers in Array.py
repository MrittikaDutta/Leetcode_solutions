from math import gcd
from typing import List
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for x in nums:
            stack.append(x)
            # keep merging while top two are non-coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break  # coprime, stop
                # merge
                lcm = a * b // g
                stack.pop()
                stack.pop()
                stack.append(lcm)
        
        return stack
