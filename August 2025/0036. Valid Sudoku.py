from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell_value = board[r][c]

                if cell_value == ".":
                    continue
                box_index = (r // 3) * 3 + (c // 3)
                if cell_value in rows[r] or \
                   cell_value in cols[c] or \
                   cell_value in boxes[box_index]:
                    return False

                rows[r].add(cell_value)
                cols[c].add(cell_value)
                boxes[box_index].add(cell_value)

        return True
