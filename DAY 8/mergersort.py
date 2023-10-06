def merge(nums,i,j):
    if i<j:
        mid= (i+j)//2
        merge(nums,i,mid)
        merge(nums,mid+1,j)
        nums[i:j+1] = mergesort(nums,i,mid,j)
def mergesort(nums, st, mid, end):
    i = st
    j = mid + 1
    res = []

    while i <= mid and j <= end:
        if nums[i] < nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1

    while i <= mid:
        res.append(nums[i])
        i += 1

    while j <= end:
        res.append(nums[j])
        j += 1

    return  res

nums = [4, 1, 2, 5, 6]
merge(nums, 0, len(nums) - 1)
print(nums)
    
