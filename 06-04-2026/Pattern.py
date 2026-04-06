## Pattern Printing
## n = 5


def is_PatternPrinting(n: int):
    if n < 0:
        return "Invalid Input"
    else:
        for i in range(1, n+1,+1):
            print(" "* (n-i) + "* " * i)
        for j in range(n, 0, -1):
            print(" "* (n-j)+ "* "* j)

is_PatternPrinting(4)