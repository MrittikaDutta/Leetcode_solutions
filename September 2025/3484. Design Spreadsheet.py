class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        expr = formula[1:]
        left, right = expr.split('+')
        def parse(token: str) -> int:
            token = token.strip()
            if token and token[0].isalpha():
                return self.cells.get(token, 0)
            return int(token)
        
        return parse(left) + parse(right)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
