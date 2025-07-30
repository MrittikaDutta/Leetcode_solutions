# 2419. Longest Subarray With Maximum Bitwise AND
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        longest = 0
        current_length = 0
        for i in nums:
            if i == m:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0 

        return longest
