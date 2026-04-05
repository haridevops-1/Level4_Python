# Create a function `commonElements` that takes two "sorted" arrays of numbers and returns an array of numbers which are common to both the input arrays.
# Examples:
# commonElements([1, 3, 4, 6, 7, 9], [-1, 3]) ➞ [3]
# commonElements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]) ➞ [1, 3, 4, 7]
# commonElements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]) ➞ [1, 2, 4, 5]
# commonElements([1, 2, 3, 4, 5], [10, 12, 13, 15]) ➞ []

def containingDuplicates(num1, num2):
    # if len(num1) or len(num2) == 0:
    #     return "Invalid Input"
    # else:
        result = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                if num1[i] == num2[j]:
                    result.append(num1[i])
                    
        return result

print(containingDuplicates([1, 3, 4, 6, 7, 9], [-1, 3]))