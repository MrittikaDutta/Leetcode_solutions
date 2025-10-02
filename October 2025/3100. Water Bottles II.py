class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            # exchange empties for 1 new bottle
            empty -= numExchange
            numExchange += 1
            # drink that bottle
            drunk += 1
            empty += 1
        
        return drunk
