# To Find Leaders

# Example:
# Input: [16,17,4,3,5,2]
# Output: [17,5,2]


def is_toFindLeaders(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        result = []
        for i in range(0, len(arr), +1):
            max = 0
            for j in range(i + 1, len(arr), +1):
                if arr[j] > max:
                    max = arr[j]
            # print(arr[i],max)
            if arr[i] > max:
                result.append(arr[i])
        return result


print(is_toFindLeaders([16, 17, 4, 3, 5, 2]))
