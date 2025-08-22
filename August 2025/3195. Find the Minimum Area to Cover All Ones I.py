class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row, max_row = math.inf, -1
        min_col, max_col = math.inf, -1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    min_row = min(min_row, r)
                    max_row = max(max_row, r)
                    min_col = min(min_col, c)
                    max_col = max(max_col, c)

        height = max_row - min_row + 1
        width = max_col - min_col + 1
        return height * width
