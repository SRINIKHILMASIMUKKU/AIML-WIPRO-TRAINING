def binary(arr, tar):
    left = 0
    right=len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary([1,2,3,4,5,6,7],  4))
