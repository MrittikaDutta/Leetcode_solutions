class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        clean = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                clean.append(nums[i])

        count = 0
        # Iterate from 1 to len-2 to ensure neighbors exist
        for i in range(1, len(clean) - 1):
            if clean[i] > clean[i - 1] and clean[i] > clean[i + 1]:
                count += 1  # hill
            elif clean[i] < clean[i - 1] and clean[i] < clean[i + 1]:
                count += 1  # valley

        return count
