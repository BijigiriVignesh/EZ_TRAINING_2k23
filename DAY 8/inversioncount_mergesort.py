def merge(nums, i, j):
    if i < j:
        mid = (i + j) // 2
        inversion = 0  
        inversion += merge(nums, i, mid)  
        inversion += merge(nums, mid + 1, j)  
        inversion += merge_and_count_inversions(nums, i, mid, j)  
        return inversion

    return 0

def merge_and_count_inversions(nums, i, mid, j):
    left = nums[i:mid + 1]
    right = nums[mid + 1:j + 1]

    k = i
    inversion = 0
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            nums[k] = left[left_idx]
            left_idx += 1
        else:
            nums[k] = right[right_idx]
            right_idx += 1
            inversion += (mid - i + 1) - left_idx  # Count inversions

        k += 1

    while left_idx < len(left):
        nums[k] = left[left_idx]
        left_idx += 1
        k += 1

    while right_idx < len(right):
        nums[k] = right[right_idx]
        right_idx += 1
        k += 1

    return inversion

nums = [3, 1, 2, 4, 5]
inversions = merge(nums, 0, len(nums) - 1)
print("Number of inversions:", inversions)
print("Sorted Array:", nums)
