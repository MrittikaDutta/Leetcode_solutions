
import math
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        # Convert integers to floats for real division
        nums = [float(card) for card in cards]
        return self.solve(nums)

    def solve(self, nums: List[float]) -> bool:
        if not nums:
            return False
        
        # Base case: if only one number is left, check if it's 24
        if len(nums) == 1:
            return math.isclose(nums[0], 24.0, abs_tol=1e-6)

        # Iterate through all pairs of numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                
                # Pick two numbers to operate on
                a = nums[i]
                b = nums[j]
                
                # Create a new list with the remaining numbers
                new_nums = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        new_nums.append(nums[k])

                # Try all possible operations
                # The order of operations does not matter for addition and multiplication
                # so we can avoid redundant checks. For subtraction and division, order matters.
                
                # Addition
                if self.solve(new_nums + [a + b]):
                    return True
                
                # Subtraction (a - b)
                if self.solve(new_nums + [a - b]):
                    return True
                
                if self.solve(new_nums + [a - b]):
                    return True
                
                # Subtraction (b - a)
                if self.solve(new_nums + [b - a]):
                    return True
                    
                # Multiplication
                if self.solve(new_nums + [a * b]):
                    return True
                
                # Division (a / b)
                if b != 0:
                    if self.solve(new_nums + [a / b]):
                        return True
                
                # Division (b / a)
                if a != 0:
                    if self.solve(new_nums + [b / a]):
                        return True
        
        # If no combination leads to 24
        return False
