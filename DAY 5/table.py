def table(n,i):
    if i > 10:
        return
    print(n*i)
    table(n,i+1)
table(5,1)
