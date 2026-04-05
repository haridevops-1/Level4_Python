def ShiftZeroToLast(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        count = 0
        result = []
        for i in range(0, len(arr), +1):
            if arr[i] != 0:
                result.append(arr[i])
            else:
                count = count + 1
        for j in range(0, count, +1):
            result.append(0)
        return result


print(ShiftZeroToLast([1, 2, 4, 0, 5, 0, 3, 0]))
