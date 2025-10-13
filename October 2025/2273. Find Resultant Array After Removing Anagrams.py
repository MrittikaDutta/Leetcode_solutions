class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for word in words:
            if not stack or sorted(stack[-1]) != sorted(word):
                stack.append(word)
        return stack
