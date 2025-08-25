class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1 for up-right, -1 for down-left

        while len(result) < m * n:
            result.append(mat[row][col])

            if direction == 1:
                # Move up-right
                row -= 1
                col += 1

                # Check for boundary conditions
                if col >= n:  # Hit the right edge
                    row += 2  # Adjust row back to valid position
                    col = n - 1 # Reset col
                    direction = -1
                elif row < 0:  # Hit the top edge
                    row = 0
                    direction = -1
            else:  # direction == -1
                # Move down-left
                row += 1
                col -= 1

                # Check for boundary conditions
                if row >= m:  # Hit the bottom edge
                    col += 2  # Adjust col back to valid position
                    row = m - 1 # Reset row
                    direction = 1
                elif col < 0:  # Hit the left edge
                    col = 0
                    direction = 1
        
        return result
