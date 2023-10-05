def subsetsum(nums,target,n,sum):
    print(sum , target)
    if sum == target:
        return True
    if n == len(nums) or sum >target:
        return False
    return subsetsum(nums,target, n+1,sum) or subsetsum(nums,target, n+1,sum+nums[n])
nums = [3, 34, 4, 12, 5, 2]
target = 14
print(subsetsum(nums,target,len(nums),0))