def magicsquare(n):
    mat = [[0]*n for i in range(n)]
    num =1
    i =n//2
    j = n-1
    while(num <= n*n):
        if i <0 and j == n:
            i = 0
            j = n-2
        else:
            if i <0:
                i = n-1
            if j == n:
                j=0
        if mat[i][j]:
            i +=1
            j -= 2
            continue
        mat[i][j] = num
        num+=1
        i -=1
        j +=1
    return mat
print(magicsquare(3))


