class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        height = [0] * n
        total = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            stack = []
            sum_in_row = [0] * n
            for j in range(n):
                while stack and height[stack[-1]] >= height[j]:
                    stack.pop()
                if stack:
                    prev = stack[-1]
                    sum_in_row[j] = sum_in_row[prev] + height[j] * (j - prev)
                else:
                    sum_in_row[j] = height[j] * (j + 1)
                stack.append(j)
                total += sum_in_row[j]
        
        return total
