class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:  # all digits same
                if sub > max_good:          # lexicographical comparison works for equal length
                    max_good = sub
        return max_good
