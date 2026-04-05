def selection_sort(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        for i in range(0,len(num),+1):
            min_index = i
            for j in range(i+1, len(num),+1):
                if num[i + 1] > num[min_index]:
                    return num[i]
                    num[min_index] = num[i+1]
                    temp = num[min_index]
                    num[min_index] = num[i]
                    num[i] = temp
print(selection_sort([50,40,30,20,10]))

