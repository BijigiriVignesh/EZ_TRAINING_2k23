def generate(nums, target):
    res = []
    usable ={}
    for i in nums:
        usable[i] = True
    def coins(nums, target, n, l):
        if target == 0:
            res.append(l)
            return
        if n == 0 or target < 0:
            return
        coins(nums, target, n - 1, l)
        if usable[nums[i]]:
            l.append(nums[n - 1])
            usable[nums[i]] = False
            coins(nums, target - nums[n - 1], n, l)
    coins(nums, target, len(nums), [])
    return res

coin = [1, 2, 5]
target = 5
result = generate(coin, target)
print(result)
