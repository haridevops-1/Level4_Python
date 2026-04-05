# * * * *
# * * * *
# * * * *
# * * * *


def square_pattern(n):
    if n == 0:
        print("Invalid Input")
    else:
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()


square_pattern(5)


