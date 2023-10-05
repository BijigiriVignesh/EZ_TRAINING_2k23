n=3

mat = [[0]*n for _ in range(n)]
def generate(i,j,num):
    if num  > n*n:
        return mat
    if i < 0 and j ==n:
        i = 0
        j = n-2
    else:
        if i <0:
            i = n-1
        if j == n:
            j = 0
    if mat[i][j]:
        return  generate(i+1,j-2,num)
    mat[i][j] = num
    return generate(i-1,j+1,num+1)
print(generate(0,0,1))


