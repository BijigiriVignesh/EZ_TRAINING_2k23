def squrt(target,i,j):
    if j - i < 0.00000001:#if the error is so minimal we return as the i and j values wont be same for any nymber of rexursions.
        
        return i
    mid = (i+j)/2
    if mid *mid==target:
        return mid
    if mid *mid>target:
        return squrt(target,i,mid)
    if mid *mid<target:
        return squrt(target,mid,j)
n = 10
print(squrt(n,0,n))