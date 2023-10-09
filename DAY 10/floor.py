def floor(nums,target,i,j):
    print(nums,i,j)
    if i >j:
        return 
    mid = (i+j) //2
    if nums[mid] == target:
        return mid
    if i == j:
        return i
    if nums[mid] > target:
        return floor(nums,target,i,mid-1)
    if nums[mid] < target and nums[mid+1] > target:
        return mid
#floor with linear search.
nums = [2,3,4,7]
print(floor(nums,5,0,5))
def lfloor(nums,target,i,j):
    for i in range(len(nums)):
        if nums[i]==target:
            return nums[i]
        if nums[i] > target:
            return nums[i-1]
nums = [2,4,7,8]
print(lfloor(nums,5))
        


    