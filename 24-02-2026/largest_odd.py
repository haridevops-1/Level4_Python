# Given a list of Integers, find teh largest odd number.


def is_largestOdd(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        odd_num = []
        even_num = []
        for i in range(0, len(arr), +1):
            if arr[i] % 2 != 0:
                odd_num.append(arr[i])
            else:
                even_num.append(arr[i])
        if len(even_num) == len(arr):
            return "No odd Number"
        # print(odd_num)
        max_odd = 0
        for j in range(0, len(odd_num), +1):
            if odd_num[j] > max_odd:
                max_odd = odd_num[j]
        return max_odd


print(is_largestOdd([2, 4, 6, 7, 10, 9]))
print(is_largestOdd([2, 4, 6, 7, 10, 9,11]))
print(is_largestOdd([2, 4, 6, 8]))
