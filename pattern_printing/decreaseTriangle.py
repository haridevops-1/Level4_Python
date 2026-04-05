def is_decreasePrint(n):
    if n == 0:
        return "Invalid Input"
    else:
        for i in range(n):
            for j in range(i, n):
                print("*", end=" ")
            print()


is_decreasePrint(5)
