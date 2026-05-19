# Example:
# Input n = 4
# output:   # 4 3 2 1
# 3 2 1
# 2 1
# 1


def NumberPattern(n: int):
    for i in range(n, 0, -1):
        for j in range(n):
            temp = i - j
            if temp >= 1:
                print(temp, end=" ")
        print()


NumberPattern(4)
