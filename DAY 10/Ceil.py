def ceil(nums,target,i,j):
    print(nums,i,j)
    if i >j:
        return 
    mid = (i+j) //2
    if nums[mid] == target:
        return mid
    if i == j:
        return i
    if nums[mid] > target:
        return ceil(nums,target,i,mid-1)
    if nums[mid] < target:
        return ceil(nums,target,mid+1,j)
nums = [2,3,4,7]
print(ceil(nums,5,0,0))

#ceil with linear search.
def lceil(nums,target,i,j):
    for i in range(len(nums)):
        if nums[i]==target:
            return nums[i]
        if nums[i] > target:
            return nums[i]
nums = [2,4,7,8]
print(lceil(nums,5))
        
    