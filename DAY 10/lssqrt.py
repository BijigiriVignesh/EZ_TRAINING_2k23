def lssqrt(nums,target,i):
    if nums[i] * nums[i] > target:
        return i-1
    if nums[i] * nums[i] == target:
        return i
    if i == len(nums)-1:
        return i
    return lssqrt(nums,target,i+1)
n =25
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(1,n//2+1):
    nums.append(i)
print(nums)
print(lssqrt(nums,n,0))
    