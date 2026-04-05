# time complexity : O (n ^ 2)


def bubble_sort(arr):
    if len(arr) == 0:
        return "invalid input"
    else:
        # sorting
        # while loop with for loop
        swapped = True  # boolean

        while swapped == True:  # start to end
            swapped = False
            for i in range(0, len(arr) - 1, +1):  # start from 40 till 60
                if arr[i] > arr[i + 1]:
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
                    # change from false to true
                    swapped = True
        print(arr)
        return arr


bubble_sort([40, 10, 30, 20, 60, 80])
bubble_sort([0, 20, 100, 12, 12, 5, 0])  # [0,0,5,12,12,20,100]
bubble_sort([1, 3, 1, 4])  # [1,1,3,4]
