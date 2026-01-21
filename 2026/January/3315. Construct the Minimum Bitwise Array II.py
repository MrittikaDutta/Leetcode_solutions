class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            if n == 2:
                ans.append(-1)
                continue
            
            # Find the first 0 bit from the right.
            # Since n is prime and > 2, it's always odd (ends in 1).
            # We look for the end of the trailing set bits.
            for i in range(31):
                # Check if the (i+1)-th bit is 0
                if not (n & (1 << (i + 1))):
                    # Flip the i-th bit from 1 to 0
                    ans.append(n ^ (1 << i))
                    break
        return ans
