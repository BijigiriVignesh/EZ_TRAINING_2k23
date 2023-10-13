def knapsack(wt,pt,n,knap):
    dp =[]
    for i in range(n+1):
        dp.append([0]*(knap+1))
    for i in range(n+1):
        for w in range(knap+1):
            if i == 0 or w == 0:
                pass
            elif wt[i-1]<=w:
                diff = w - wt[i-1]
                dp[i][w] = max(pt[i-1]+dp[i-1][diff],dp[i-1][w])
            else :
                dp[i][w] = dp[i-1][w]
    print(dp[n][knap])
knapsack([2,5,4,1,3],[70,90,40,120,80],5,10)
