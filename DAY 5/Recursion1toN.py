def printing(n):
    if (n == 0):
        return
    printing(n-1) #head recursion 
    print(n) #printing the n value
n = int(input())
printing(n)