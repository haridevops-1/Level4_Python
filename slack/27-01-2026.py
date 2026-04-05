# 3. Find the number of instances of a substring in a string without using any library functionsstring
# - this is an islandsubstring - isnumber of instances 3


def library_string(text: str):
    if len(text) == 0:
        return "Invalid Input"
    else:
        count = 0
        a = text.split(" ")
        # return a
        for i in range(len(a)):
            # print(a[i])
            if "is" in a[i]:
                count = count + 1
        return count


print(library_string("this is an islaisnd"))

# Given a two dimensional array find the maximum and minimum in it and print


def twoDimensionalArray(num):
    if len(num) == 0:
        return "Invalid Input"
    else:
        maximum = num[0][0]
        minimum = num[0][0]
        for i in num:
            for j in i:
                if j > maximum:
                    maximum = j
                if j < minimum:
                    minimum = j
        return (maximum, minimum)


print(twoDimensionalArray([[3, 5, 1], [9, 2, 8], [4, 6, 7]]))


# Given a value of N print the below pattern N = 3
def pattern(n):
    for i in range(n):
        for j in range(2):
            print("*", end=" ")
        print()


pattern(3)
