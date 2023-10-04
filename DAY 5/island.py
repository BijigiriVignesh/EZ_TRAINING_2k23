def traverse(m, i, j):
    if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]) or m[i][j] == 0:
        return 
    m[i][j] = 0
    traverse(m, i, j + 1 )
    traverse(m, i, j - 1)
    traverse(m, i - 1, j)
    traverse(m, i + 1, j)
def countIslands(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                island_count += 1
                traverse(grid, i, j)
    return island_count

grid= [[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]]
print(countIslands(grid))
