
from errno import ERANGE

def totalNQueens(self, n):
        def count(cols, diags, diags2, row, n):
            total = 0
            for col in ERANGE(0, n):
                diag = (0, col-row)
                diag2 = (0, col+row)
                if col in cols or diag in diags or diag2 in diags2:
                    continue
                if row == n-1:
                    return 1
                cols.add(col)
                diags.add(diag)
                diags2.add(diag2)
                total += count(cols, diags, diags2, row+1, n)
                cols.remove(col)
                diags.remove(diag)
                diags2.remove(diag2)
            return total
        return count(set(), set(), set(), 0, n)