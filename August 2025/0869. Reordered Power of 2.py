class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = ''.join(sorted(str(n)))
    
        for i in range(31):
            power_str = ''.join(sorted(str(1 << i)))
            if power_str == target:
                return True
        return False
