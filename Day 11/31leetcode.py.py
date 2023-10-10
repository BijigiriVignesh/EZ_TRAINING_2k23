def bs(ele,nums):
    l = 0
    r = len(nums)-1
    while(l<=r):
        mid = (l+r) //2
        if(nums[mid] == ele):
            return mid
        elif (nums[mid] >ele):
            r= mid-1
        else:
            l =mid+1
    return -1

def tripletsum(nums,k):
    nums.sort()
    l = 0
    r = len(nums) -1
    while(l<=r):
        diff = k-(nums[l]+nums[r])
        if(diff >0):
            k = bs(diff,nums)
            if(k!=-1):
                return [l,r,k]
        else:
            r -=1

        
nums = [1,2,4,9,12]
target =15
print(tripletsum(nums,target))

