// gfg
class Solution {
  public:
    int nonLisMaxSum(vector<int>& arr) {
        // code here
        int n = arr.size();
    vector<vector<int>> dp(n, vector<int>(2));

    for (int i = 0; i < n; ++i) {
        // Initialize base sum and base length
        dp[i][0] = arr[i];
        dp[i][1] = 1;

        for (int j = 0; j < i; ++j) {
            if (arr[i] > arr[j]) {
                // same length LIS can be formed
                // choose the one with smaller sum
                if (dp[j][1] + 1 == dp[i][1]) {
                    dp[i][0] = min(dp[i][0], dp[j][0] + arr[i]);
                }
                // longer LIS can be formed, update both length and sum
                else if (dp[j][1] + 1 > dp[i][1]) {
                    dp[i][0] = dp[j][0] + arr[i];
                    dp[i][1] = dp[j][1] + 1;
                }
            }
        }
    }

    // find maximum LIS length
    int maxLen = 0;
    for (int i = 0; i < n; ++i) {
        maxLen = max(maxLen, dp[i][1]);
    }

    // find minimum sum among LIS of maximum length
    int minSum = INT_MAX;
    for (int i = 0; i < n; ++i) {
        if (dp[i][1] == maxLen) {
            minSum = min(minSum, dp[i][0]);
        }
    }

    int total = accumulate(arr.begin(), arr.end(), 0);

    return total - minSum;
    }
};
