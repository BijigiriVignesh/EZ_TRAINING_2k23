def coinchange(coins, target):
    n = len(coins)
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

    return dp[n][target]

result = coinchange([2, 5], 11)
print(result)
