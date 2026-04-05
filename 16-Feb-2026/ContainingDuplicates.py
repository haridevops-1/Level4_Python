def ContainingDuplicates(nums: list[int]):
    if len(nums) == 0:
        return "Invalid Input"
    else:
        repeat = []
        for i in range(0, len(nums), +1):
            if nums[i] not in repeat:
                repeat.append(nums[i])
        if len(repeat) == len(nums):
            return False
        return True


print(ContainingDuplicates([1, 2, 3, 1]))
