# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input : [1,3,2,5] , Output => 4 because 4 is the missing number in the series 1,2,3,5


def is_MissingNumber(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        max = num[0]
        for i in range(0, len(num), +1):
            if num[i] > max:
                max = num[i]
        for j in range(1, max + 1, +1):
            if j not in num:
                return j


print(is_MissingNumber([1, 3, 2, 5]))
