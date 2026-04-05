# Sub-task- To Find which number is greater

# Input: [1,2,2,3,2,4,5,2,3,4,5,6]
# output: [2]


def is_maximumNumbers(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        dict = {}
        for i in range(0, len(num), +1):
            if num[i] in dict:
                dict[num[i]] += 1
            else:
                dict[num[i]] = 1
        # return dict
        max_count = 0
        for key in dict:
            if dict[key] > max_count:
                max_count = dict[key]
                max_key = key
        return max_key


print(is_maximumNumbers([1, 2, 2, 3, 3, 3, 3, 4, 5, 2, 3, 4, 5, 6]))
