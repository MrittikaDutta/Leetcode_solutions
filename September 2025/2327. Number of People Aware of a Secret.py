class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        
        sharers_count = 0
        
        for i in range(2, n + 1):
            if i - delay >= 1:
                sharers_count = (sharers_count + dp[i - delay]) % MOD
            
            if i - forget >= 1:
                sharers_count = (sharers_count - dp[i - forget] + MOD) % MOD
            dp[i] = sharers_count
            
        total_aware = 0
        for i in range(max(1, n - forget + 1), n + 1):
            total_aware = (total_aware + dp[i]) % MOD
            
        return total_aware
