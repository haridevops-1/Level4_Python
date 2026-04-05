# 2D Array
# Input: [[1,2][3,4],[5,6]]
# Output: [[1,3,5],[2,4,6]]


def is_2D_Array(arr):
    if len(arr) == 0:
        return "Invalid Input"

    result = []

    # number of columns
    for i in range(len(arr[0])):
        temp = []

        # number of rows
        for j in range(len(arr)):
            temp.append(arr[j][i])

        result.append(temp)

    return result


print(is_2D_Array([[1, 2], [3, 4], [5, 6]]))
