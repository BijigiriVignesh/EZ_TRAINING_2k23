num = int(input())
c0 = 0
c1 = 0
flag = True
while num>0:
    if num%2==0:
        c0+=1
    else:
        c1+=1
    if c1>1:
        flag = False
    num//=2
if flag and c0%4==0:
    print("yes")
else:
    print("no")
'''
Other methods :
to check for the power of 2 :
    if a & (a-1):
        print(true)
    else:
        print(False)
To check for power of 4 :
if a & (a-3):
print true
else
print false
'''