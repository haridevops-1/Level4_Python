# Rearrange the array into odd or even

# Input: [3,1,2,4,5]
# Output: [4,2,1,3]


def Rearrange_oddEven(arr: list[int]):
    if len(arr) == 0:
        return "Invalid Input"
    else:
        odd = []
        even = []

        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                even.append(arr[i])
            else:
                odd.append(arr[i])

        return even + odd   
print(Rearrange_oddEven([3,1,2,4,5]))


### Approach- 2

def Rearrange_withinList(num: list[int]):
    if len(num) == 0:
        return "Invalid Input"
    else:
        left = 0
        for right in range(len(num)):
            if num[right] % 2 == 0:
                num[left], num[right] = num[right], num[left]
                left+= 1
        return num
    
print(Rearrange_withinList([3,5,6,7,2,4,56,]))