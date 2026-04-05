def findingLinearSearch(numbers, target) -> int:

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


numbers = [100, 30, 20, 40, 50, 50]
target = 50

output = findingLinearSearch(numbers, target)
print(f"{target} is found at {output}")

