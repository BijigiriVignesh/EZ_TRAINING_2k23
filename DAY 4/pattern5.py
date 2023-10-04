n = int(input())
for i in range(1,n+1):
    res = 0
    j = i
    while(j):
        res += (10 ** (j-1))*i
        j-=1
    print(res)