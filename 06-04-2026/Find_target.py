## To find Target
## Example:

## arr = [5,3,4,1,2,0]
## output : [1,5]


def is_FindTarget(arr: list[int], target: int):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        result = []
        for i in range(0, len(arr) - 1, +1):
            temp = arr[i]
            for j in range(i + 1, len(arr), +1):
                if temp + arr[j] == target:
                    print(i, j)
                    return
        print(-1)


is_FindTarget([5, 3, 4, 1, 2, 0], 3)
is_FindTarget([4, 1, 7, 3], 3)
