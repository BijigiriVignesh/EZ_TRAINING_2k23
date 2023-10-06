def qsort(nums,st,end):
    pivot = nums[end]
    i = st-1
    for j in range(st,end):
        if nums[j] < pivot:
            i+=1
            nums[i],nums[j] =nums[j],nums[i]
    nums[i+1],nums[end] = nums[end],nums[i+1]
    return i+1
def quick(nums,st,end): 
    if(st<end):
        pivot = qsort(nums,st,end)
        quick(nums,st,pivot-1)
        quick(nums,pivot+1,end)
nums = [5,1,3,2,6]
quick(nums,0,len(nums)-1)
print(nums)