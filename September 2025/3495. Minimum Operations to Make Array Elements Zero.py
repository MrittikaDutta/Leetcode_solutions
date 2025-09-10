# 3495. Minimum Operations to Make Array Elements Zero


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res=0
        def S(n: int) -> int:
            
            if n < 1:
                return 0
            total = 0
            d = 1
            while True:
                lo = 4 ** (d - 1)
                hi = 4 ** d - 1
                if lo > n:
                    break
                c= min(n, hi) - lo + 1
                total += d * c
                d += 1
            return total
    
        for l, r in queries:
            ss= S(r) - S(l - 1)
            ops = (ss+ 1)//2
            res += ops
        
        return res
