from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        freq = Counter(s)

        mvf = max((freq[char] for char in vowels if char in freq), default=0)
        mcf = max((freq[char] for char in freq if char not in vowels), default=0)

        return mvf + mcf
