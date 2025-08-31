class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    v = board[i][j]
                    rows[i].add(v)
                    cols[j].add(v)
                    boxes[(i // 3) * 3 + (j // 3)].add(v)

        def backtrack(k=0):
            if k == len(empty):
                return True
            r, c = empty[k]
            b = (r // 3) * 3 + (c // 3)
            for v in map(str, range(1, 10)):
                if v not in rows[r] and v not in cols[c] and v not in boxes[b]:
                    board[r][c] = v
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[b].add(v)

                    if backtrack(k + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxes[b].remove(v)
            return False

        backtrack()
