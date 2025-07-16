class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even_count = sum(1 for x in nums if x % 2 == 0)
        odd_count = len(nums) - even_count
        same_parity_max = max(even_count, odd_count)
        
        # Case 2: Alternating parity subsequence
        
        def longest_alternating(start_parity):
            count = 0
            curr_parity = start_parity
            for num in nums:
                if num % 2 == curr_parity:
                    count += 1
                    curr_parity ^= 1 # flip between 0 and 1
            return count
        
        alt1 = longest_alternating(0)  # start with even
        alt2 = longest_alternating(1)  # start with odd
        alternating_max = max(alt1, alt2)
        
        return max(same_parity_max, alternating_max)
