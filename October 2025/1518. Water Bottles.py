class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        b=numBottles
        i=numBottles
        ne=numExchange
        while i>=ne:
            n=i//ne
            i=i%ne+n
            b+=n
        return b
