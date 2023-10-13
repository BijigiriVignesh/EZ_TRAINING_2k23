def coinchange(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    return dp[target]
result = coinchange([3, 5], 12)
print(result)
