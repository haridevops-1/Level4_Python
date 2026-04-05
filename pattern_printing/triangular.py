# Write a python function `print_pattern(n:int)` ,

# Given a number n=4, print the below pattern


# 1
# 1 2
# 1 2 3
# 1 2 3 4

# BONUS: if completed, print the same in reverse order (inverted triangle)


def print_pattern(n: int):
    for i in range(1, n + 1):  # Outer loop (rows)
        for j in range(1, i + 1):  # Inner loop (numbers)
            print(j, end=" ")
        print()  # Move to next line
