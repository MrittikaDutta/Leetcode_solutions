class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        list_s = list(s)

        for i in range(len(list_s)):
            if list_s[i] == '6':
                list_s[i] = '9'
                break

        return int("".join(list_s))
