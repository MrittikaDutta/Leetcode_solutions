class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_count = 0
        for char in s:
            if char in vowels:
                vowel_count += 1
        if vowel_count == 0:
            return False
        
        
        return True
