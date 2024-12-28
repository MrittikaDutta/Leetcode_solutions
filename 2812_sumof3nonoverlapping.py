class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Compute the sum of all k-length subarrays
        window_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sum[0] = current_sum
        for i in range(1, len(window_sum)):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sum[i] = current_sum

        # Step 2: Precompute the best indices for left and right subarray sums
        left = [0] * len(window_sum)
        best_left = 0
        for i in range(len(window_sum)):
            if window_sum[i] > window_sum[best_left]:
                best_left = i
            left[i] = best_left

        right = [0] * len(window_sum)
        best_right = len(window_sum) - 1
        for i in range(len(window_sum) - 1, -1, -1):
            if window_sum[i] >= window_sum[best_right]:
                best_right = i
            right[i] = best_right

        # Step 3: Find the maximum sum of three subarrays
        max_sum = 0
        result = []
        for middle in range(k, len(window_sum) - k):
            l = left[middle - k]
            r = right[middle + k]
            total = window_sum[l] + window_sum[middle] + window_sum[r]
            if total > max_sum:
                max_sum = total
                result = [l, middle, r]

        return result
