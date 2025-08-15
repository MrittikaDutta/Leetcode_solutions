class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        a=n
        if n==1:
            return True
        k=1
        while k<a:
            k=k*4
            if k==a:
                return True
        return False
