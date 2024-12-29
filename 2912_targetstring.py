class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for j, char in enumerate(word):
                freq[j][ord(char) - ord('a')] += 1
        
        dp = [0] * (m + 1)
        dp[0] = 1
        for j in range(n):
            for i in range(m, 0, -1):
                char_index = ord(target[i-1]) - ord('a')
                dp[i] = (dp[i] + dp[i-1] * freq[j][char_index]) % MOD
        
        return dp[m]
