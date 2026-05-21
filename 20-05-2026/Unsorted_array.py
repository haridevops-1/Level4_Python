# Question 3:

# Given an unsorted integer array, find a pair with the given sum in it.
# You can Use two or more approaches in the problem (e.g. brute force, using dictionaries)
# For example,

# Input:
# nums = [8, 7, 2, 5, 3, 1]
# target = 10

# Output:
# Pair found (8, 2) or
# Pair found (7, 3)


def is_UnsortedArray(nums: list[int], target: int):
    if len(nums) == 0:
        return "Invalid Input"
    else:
        result = []
        for i in range(0, len(nums), +1):
            for j in range(i + 1, len(nums), +1):
                if nums[i] + nums[j] == target:
                    result.append((nums[i], nums[j]))
        return result


print(is_UnsortedArray([8, 7, 2, 5, 3, 1], 10))
