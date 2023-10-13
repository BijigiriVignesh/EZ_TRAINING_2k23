def rotate(arr, k):
    n = len(arr)
    k%=n
    i = k+1
    j = 0
    while(k):
        arr[i] ,arr[j] = arr[j],arr[i]
        k-=1
        i+=1
        j+=1
    return arr
print(rotate([1,2,3,4,5,6,7], 3))
