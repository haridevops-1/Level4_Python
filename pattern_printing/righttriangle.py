def is_rightTriangle(n):
    if n == 0:
        return "Invalid Input"
    else:
        for i in range(n):
            for j in range(i+1):
                print("*", end=" ")
            print()

is_rightTriangle(5)