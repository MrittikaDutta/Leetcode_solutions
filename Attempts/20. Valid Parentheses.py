class Solution:
    def isValid(self, s: str) -> bool:
        st=s
        stack = []
        m = {')': '(', '}': '{', ']': '['}
        for i in st:
            if i in m:
                top_element = stack.pop() if stack else '#'
                if m[i] != top_element:
                    return 0
            else:
                stack.append(i)
        
        return not stack
