def histogram(l):
    histo=[]
    m = max(l)
    n =len(l)
    for i in l:
        histo.append([' ']*(m-i)+["*"]*(i))
    for i in range(m):  
        for j in range(n):
            print(histo[j][i], end=" ")
        print()
histogram([2,3,4])