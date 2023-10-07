global_max = float('-inf')
def recursion(nums,i,j):
    print(nums,i,j)
    if i ==j:
        return nums[i]
    if i>j:
        return
    mid = (i+j) //2
    m1 = recursion(nums,i,mid)
    m2 = recursion(nums,mid+1,j)
    return m1 if m1>m2 else m2
print("max of [2,3,5,1] is ",recursion([2,3,4,1],0,3))