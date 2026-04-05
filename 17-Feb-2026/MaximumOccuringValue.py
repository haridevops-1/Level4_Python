def MaximumValue(nums: list[int]):
    if len(nums) == []:
        return "Invalid Input"
    if len(nums) == 1:
        return nums[0]
    else:
        answer = nums[0]
        max_count = 1
        for i in range(0, len(nums), +1):
            curr_count = 0
            for j in range(i + 1, len(nums), +1):
                if nums[i] == nums[j]:
                    curr_count += 1
            if curr_count > max_count:
                max_count = curr_count
                answer = nums[i]
        return answer


### Using Dictionary


def maximumOccur(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    if len(arr) == 1:
        return
    else:
        keys = arr[0]
        count = 1
        for el in arr:
            if el not in count:
                count[el] = 1
            else:
                count[el] = count[el] + 1
        if count[el] > count:
            count = count[el]
            key = el
        return key


print(MaximumValue([5, 5, 4, 4, 4, 2, 3, 3]))
