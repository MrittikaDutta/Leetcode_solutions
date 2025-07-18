import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total = len(nums)

        # Left to right - maintain max heap to get smallest `n` elements sum
        left_heap = []
        left_sum = 0
        left_sums = [0] * (total + 1)

        for i in range(total):
            heapq.heappush(left_heap, -nums[i])  # max heap using negatives
            left_sum += nums[i]
            if len(left_heap) > n:
                left_sum += heapq.heappop(left_heap)  # remove largest (since it's negative)
            if i >= n - 1:
                left_sums[i] = left_sum

        # Right to left - maintain min heap to get largest `n` elements sum
        right_heap = []
        right_sum = 0
        right_sums = [0] * (total + 1)

        for i in range(total - 1, -1, -1):
            heapq.heappush(right_heap, nums[i])
            right_sum += nums[i]
            if len(right_heap) > n:
                right_sum -= heapq.heappop(right_heap)
            if total - i >= n:
                right_sums[i] = right_sum

        # Try all split points
        res = float('inf')
        for i in range(n - 1, 2 * n):
            res = min(res, left_sums[i] - right_sums[i + 1])

        return res
