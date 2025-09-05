class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            s = num1 - k * num2
            if s < k:
                continue
            if bin(s).count("1") <= k:
                return k
        return -1
