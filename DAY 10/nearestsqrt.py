def squrt(nums,target,i,j):
    if i>j:
        return j
    mid = (i+j) //2
    if nums[mid] * nums[mid] == target:
        return mid
    if nums[mid] * nums[mid] < target:
        return squrt(nums,target,mid+1,j)
    if nums[mid] * nums[mid] > target:
        return squrt(nums,target,i,mid-1)
n = 10
nums =[]
for i in range(1,n//2+1):
    nums.append(i)
print(squrt(nums,n,0,n//2))