class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1 or n==2:
            return False
        if n==1 or n==3:
            return True
        k=n
        while k>1:
            if k%3!=0:
                return False
            k=k//3
        return True
