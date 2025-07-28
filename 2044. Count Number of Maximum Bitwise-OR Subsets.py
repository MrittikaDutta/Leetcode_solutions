class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        count = 0
        n = len(nums)
        total_subsets = 1 << n  # 2^n subsets
        
        for subset in range(1, total_subsets):
            current_or = 0
            for i in range(n):
                if subset & (1 << i):  # Check if the ith element is in the subset
                    current_or |= nums[i]
            if current_or == max_or:
                count += 1
                
        return count
