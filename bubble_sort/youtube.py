def BubbleSorting(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        for i in range(0, len(arr) - 1, +1):
            for j in range(0, len(arr) - 1, +1):
                # print(arr[j])
                if arr[j] < arr[j + 1]:
                    continue
                elif arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        print(arr)


BubbleSorting([3, 4, 1, 5, 6, 2, 7, 8, 9])


## While loop for Bubble sort


def bubbleSort2(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        swap = True
        while swap:
            swap = False
            for i in range(0, len(arr) - 1, +1):
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    swap = True
        print(arr)


bubbleSort2([10, 40, 60, 20, 30, 40, 50, 80, 90])
