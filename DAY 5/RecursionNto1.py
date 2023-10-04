def printing(n):
    if (n == 0):
        return
    print(n)  #printing the n value first then the recursion
    printing(n-1) # this is tail recursion.

n = int(input())
printing(n)