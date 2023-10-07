def countsort(nums):
    count = [0]*(max(nums)+1)
    for i in nums:
        count[i]+=1
    for i in range(1,len(count)):
        count[i] += count[i-1]
    output = [0]*len(nums)
    print(count)
    for i in nums[::-1]:
            idx = count[i]
            output[idx-1] = i
            count[i]-=1
    print(output)
nums=[1,2,0,0,4,5,3]
countsort(nums)
        