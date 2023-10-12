class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        row_col=defaultdict(list)
        for row in range(9):
            for col in range(9):
                #print("rows  ",rows)
                #print("cols ",cols)
                #print("row_col ",row_col)
                if board[row][col] =='.':
                    pass
                else:
                   val = board[row][col]
                   if (row in rows[val]  
                   or col in cols[val]  or
                    (row//3,col//3)in row_col[val]) :
                       return False
                   rows[val].add(row)
                   cols[val].add(col)
                   row_col[val].append((row//3,col//3))
        return True