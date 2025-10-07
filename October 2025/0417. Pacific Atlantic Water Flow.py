class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m=len(heights)
        n=len(heights[0])
        pacific = set()
        atlantic = set()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or
                r < 0 or c < 0 or r >= m or c >= n or
                heights[r][c] < prev_height):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        for c in range(n):
            dfs(0, c, pacific, heights[0][c])       # top row
            dfs(m - 1, c, atlantic, heights[m - 1][c])  # bottom row
        
        for r in range(m):
            dfs(r, 0, pacific, heights[r][0])       # left column
            dfs(r, n - 1, atlantic, heights[r][n - 1])
        result = list(pacific & atlantic)
        return result
