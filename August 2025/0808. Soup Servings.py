class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0
        
        # Scale down to units of 25 mL
        n = (n + 24) // 25

        from functools import lru_cache

        @lru_cache(None)
        def dp(a, b):
            # Base cases
            if a <= 0 and b <= 0:  # both empty
                return 0.5
            if a <= 0:             # A empty first
                return 1.0
            if b <= 0:             # B empty first
                return 0.0
            
            return 0.25 * (
                dp(a - 4, b) +         # 100, 0
                dp(a - 3, b - 1) +     # 75, 25
                dp(a - 2, b - 2) +     # 50, 50
                dp(a - 1, b - 3)       # 25, 75
            )

        return dp(n, n)
