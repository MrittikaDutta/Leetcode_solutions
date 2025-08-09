class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        a=n
        if n==1:
            return True
        k=1
        while k<a:
            k=k*2
            if k==a:
                return True
        return False
