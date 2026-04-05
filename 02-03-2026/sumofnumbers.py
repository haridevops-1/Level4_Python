# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# TEST CASE 1: Input: nums = [2,11,15,7], target = 9
# Output: [0,3]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# TEST CASE 2: Input: nums = [3,3], target = 6
# Output: [0,1]


def is_SumOfTwoNumbers(nums: list[int], target: int):
    if len(nums) == 0 or target == 0:
        return "Invalid Input"
    else:
        result = []
        for i in range(0, len(nums), +1):
            for j in range(i+1,len(nums),+1):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result


print(is_SumOfTwoNumbers(nums=[2, 11, 15, 7], target=9))
