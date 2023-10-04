def sumofdig(n,su):
    if n == 0:
        return su
    return sumofdig(n//10 , su+n%10)
print(sumofdig(15,0))