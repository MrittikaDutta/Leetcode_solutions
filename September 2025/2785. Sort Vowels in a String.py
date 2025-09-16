class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        
        found_vowels = []
        for char in s:
            if char in vowels:
                found_vowels.append(char)
        
        # Step 2: Sort the vowels
        found_vowels.sort()
        
        # Step 3: Build the result string
        result = list(s) # Convert the string to a list of characters for mutable access
        vowel_index = 0
        
        for i in range(len(result)):
            if result[i] in vowels:
                result[i] = found_vowels[vowel_index]
                vowel_index += 1
                
        # Step 4: Join the list to form the final string
        return "".join(result)
