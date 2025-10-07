class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        
        heap = [(grid[0][0], 0, 0)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while heap:
            time, r, c = heapq.heappop(heap)
            
            if r == n - 1 and c == n - 1:
                return time
            
            if visited[r][c]:
                continue
            visited[r][c] = True
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    # Time = max(current time, elevation of next cell)
                    heapq.heappush(heap, (max(time, grid[nr][nc]), nr, nc))
