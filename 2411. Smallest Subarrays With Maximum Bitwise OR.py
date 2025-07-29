class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last = [0] * 32  # last seen index for each bit position

        for i in range(n - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i  # update the last position where this bit was seen

            max_len = 1  # default length is at least 1
            for b in range(32):
                if last[b]:
                    max_len = max(max_len, last[b] - i + 1)

            answer[i] = max_len

        return answer
