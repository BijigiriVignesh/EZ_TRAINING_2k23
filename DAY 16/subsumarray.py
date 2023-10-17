def subarraysum(arr,target):
    st = 0
    end = 0
    cur_sum = 0
    n = len(arr)
    count =0
    while(end<n):
        print(cur_sum)
        if cur_sum == target:
            return arr[st:end]
        elif cur_sum > target:
            cur_sum -= arr[st]
            st+=1
        else:
            cur_sum += arr[end]
            end +=1
print(subarraysum([2,5,6,7,8,10],18))