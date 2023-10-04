
l = [[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]]
print(l)
n = len(l)
c =0
def traverse(m,i,j,n):
    if (i < 0) or i == n or j <0 or j == n or m[i][j] ==0:
        return
    m[i][j] = 0
    traverse(m,i,j+1,n)
    traverse(m,i,j-1,n)
    traverse(m,i-1,j,n)
    traverse(m,i+1,j,n)
for i in range(n):
    for j in range(n):
        if(l[i][j] == 1):
            c += 1
            traverse(l,i,j,n)
print(c)

