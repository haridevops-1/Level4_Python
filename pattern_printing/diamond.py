# n = 5

# for i in range(1, n + 1, +1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)


def diamond_pattern(num):
    for i in range(1, num + 1, +1):
        print(" " * (num - i) + "* " * i)
    for i in range(num - 1, 0, -1):
        print(" " * (num - i) + "* " * i)


diamond_pattern(10)
