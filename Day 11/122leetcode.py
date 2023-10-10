def maxProfit(prices):
    left = 0
    right = 1
    n = len(prices)
    profit = 0
    while(right < n ):
        if prices[left] > prices[right]:
            left = right
        else:
            profit += prices[right]-prices[left]
            left+=1
        right+=1
    return  profit