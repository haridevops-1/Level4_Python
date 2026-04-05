def binarySearch(arr:list[int], target: int):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    return -1

print(binarySearch([30,50,10,60,80,100], target= 80))