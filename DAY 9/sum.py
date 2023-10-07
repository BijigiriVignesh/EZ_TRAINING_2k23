global_sum = 0
def recursion(nums,i,j):
    print(nums,i,j)
    if i ==j:
        return nums[i]
    if i>j:
        return
    mid = (i+j) //2
    m1 = recursion(nums,i,mid)
    m2 = recursion(nums,mid+1,j)
    return m1+m2
print("sum of [2,3,4,1] is ",recursion([2,3,4,1],0,3))