def countGoodStrings(low: int, high: int, zero: int, one: int) -> int:
    MOD = 10**9 + 7
    
    # Initialize DP array
    dp = [0] * (high + 1)
    dp[0] = 1  # Base case: one way to construct an empty string
    
    # Fill DP array
    for i in range(1, high + 1):
        if i >= zero:
            dp[i] = (dp[i] + dp[i - zero]) % MOD
        if i >= one:
            dp[i] = (dp[i] + dp[i - one]) % MOD
    
    # Count good strings
    result = 0
    for i in range(low, high + 1):
        result = (result + dp[i]) % MOD
    
    return result
