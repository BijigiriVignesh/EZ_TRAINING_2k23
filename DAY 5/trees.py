row,col = 0,0
def traverse(m,i,j,n):
    if(m[i][j] == 0):
        print(m,i,j)
        return 
    if m[i][j] == 1:
        m[i][j] = 0
    if i >= 0:
        traverse(m,i-1,j,n)
    if i <n:
        traverse(m,i+1,j,n)
    if j >=0:
        traverse(m,i,j-1,n)
    if j<n:
        traverse(m,i,j+1,n)
    return m
m = [
    [1,0,0,1],
    [1,0,0,0],
    [1,0,1,0],
    [0,1,1,1]
]
n = len(m)
matrix = traverse(m,row,col,n)
c =0
for rows in matrix:
    c += rows.count(1)
print(c)
