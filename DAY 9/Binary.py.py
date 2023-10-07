def binary(nums,ele):
    low = 0
    high =len(nums-1)
    while(low<=high):
        mid =(low+high)//2
        if nums[mid] == ele:
            return True
        if nums[mid]>ele:
            high = mid-1
        else:
            low=high+1
    return False
print(binary([2,4,5,8],2))
