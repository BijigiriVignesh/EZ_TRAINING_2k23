def primes_inrange(n):
    nums = [1]*(n+1)
    nums[0] = nums[1] =0
    for i in range(2,n+1):
        if  nums[i]:
            for j in range(i*i,n+1,i):
                nums[j] = 0
    print(list(i for i in range(n+1) if nums[i]))
primes_inrange(10)
