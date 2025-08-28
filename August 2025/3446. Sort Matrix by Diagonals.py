class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = defaultdict(list)

        # 1. Group elements by diagonal
        for r in range(n):
            for c in range(n):
                diagonals[r - c].append(grid[r][c])

        # 2. Sort the diagonals
        for diff in diagonals:
            if diff >= 0:
                # Bottom-left triangle (including main diagonal)
                diagonals[diff].sort(reverse=True)
            else:
                # Top-right triangle
                diagonals[diff].sort()

        # 3. Place sorted elements back into a new matrix
        result = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                diff = r - c
                # Pop the first element from the sorted list for the current diagonal
                result[r][c] = diagonals[diff].pop(0)

        return result
