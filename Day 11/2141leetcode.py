def maxRunTime(n, batteries):
    batteries.sort(reverse=True) 
    total_time = 0
    remaining_batteries = batteries[:n] 
    while remaining_batteries:
        for i in range(n):
            if not remaining_batteries:
                break
            remaining_batteries[i] -= 1
            if remaining_batteries[i] == 0:
                remaining_batteries.pop(i)
                i -= 1             
        total_time += 1
    return total_time
