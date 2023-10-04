def subsetsum(nums,target,n):
    if target == 0:
        return True
    if n == 0:
        return False
    if(nums[n-1] > target):
        return subsetsum(nums,target, n-1)
    return  subsetsum(nums,target-nums[n-1], n-1)
nums = [3, 34, 4, 12, 5, 2]
target = 9
print(subsetsum(nums,target,len(nums)))