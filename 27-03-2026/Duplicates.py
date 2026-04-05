def is_ContainingDuplicates(arr: list[int]):
    # Input : [1,2,3,4] --> True
    # Input : [1,2,3,1] --> False
    if len(arr) == 0:
        return "Invalid Input"
    else:
        dict = {}
        for i in range(0, len(arr), +1):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            else:
                dict[arr[i]] += 1
        # return dict
        for key in dict:
            if dict[key] > 1:
                return False
        return True


print(is_ContainingDuplicates([1, 2, 3, 4]))
print(is_ContainingDuplicates([1, 2, 3, 4, 1]))
