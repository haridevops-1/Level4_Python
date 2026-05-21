# Question 2:

# Given an array of Integers identify the maximum occurring element.

# Example:

# Input : [5,5,4,1,1,1,6,7,8], Output : 1
# Input : [5] , Output: 5
# Input: [1,2,2,3,3] , Output : [2,3]
# Input : [], Output: ‘invalid input’


def arrayOfIntegers(num: list[int]):
    if len(num) == 0:
        return False
    if len(num) == 1:
        return num
    else:
        empty = {}
        for i in range(0, len(num), +1):
            if num[i] not in empty:
                empty[num[i]] = 1
            else:
                empty[num[i]] += 1
        # print(empty)
        max = 0
        result = ""
        for key in empty:
            if empty[key] > max:
                max = empty[key]
        return empty[key]


print(arrayOfIntegers([5, 5, 4, 1, 1, 1, 6, 7, 8]))
print(arrayOfIntegers([5]))
print(arrayOfIntegers([1, 2, 2, 3, 3]))
