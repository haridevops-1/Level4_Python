# binary search


def binary_search(arr: list[int], target: int) -> int:
    if len(arr) == 0:
        print("Invalid Input")
    else:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1


print(binary_search([20, 30, 40, 50, 60], 50))
