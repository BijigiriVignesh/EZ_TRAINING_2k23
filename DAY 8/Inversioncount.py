def inversioncount(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] >nums[j]:
                count += 1
    return count
nums = [3,1,2,4,5]
print(inversioncount(nums))